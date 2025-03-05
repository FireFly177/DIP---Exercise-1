import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image  # For handling TIFF files

# Function to apply histogram equalization (for contrast enhancement)
def enhance_image(img):
    return cv2.equalizeHist(img)  # Directly apply histogram equalization on grayscale image

# Function to add Gaussian noise
def add_gaussian_noise(img, mean=0, sigma=40):
    noise = np.random.normal(mean, sigma, img.shape).astype(np.int16)  # Use int16 to prevent overflow
    noisy_img = img.astype(np.int16) + noise
    noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)  # Ensure pixel values remain valid
    return noisy_img

# Function to apply Arithmetic Mean Filter (Averaging Filter)
def arithmetic_mean_filter(img, kernel_size=5):
    return cv2.blur(img, (kernel_size, kernel_size))

# Function to apply Geometric Mean Filter
def geometric_mean_filter(img, kernel_size=5):
    img = img.astype(np.float32) + 1  # Avoid log(0)
    log_img = np.log(img)
    mean_log = cv2.blur(log_img, (kernel_size, kernel_size))
    geometric_mean = np.exp(mean_log).astype(np.uint8)
    return geometric_mean

# Function to apply Gaussian filter for denoising
def gaussian_filter(img, kernel_size=5):
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

# Function to read images, including TIFF files
def read_image(img_path):
    ext = img_path.lower().split('.')[-1]
    
    # Use OpenCV for common formats (JPG, PNG)
    if ext in ['jpg', 'jpeg', 'png']:
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    # Use PIL for TIFF files
    elif ext in ['tif', 'tiff']:
        img = Image.open(img_path)
        img = img.convert("L")  # Convert to grayscale
        img = np.array(img)  # Convert to NumPy array for OpenCV processing
    else:
        print(f"Unsupported file format: {img_path}")
        return None
    
    return img

# Directory setup
input_folder = "images"  # Folder containing input images
output_folder = "processed_images"  # Folder to save processed images
os.makedirs(output_folder, exist_ok=True)

# Get list of image files (including TIFF)
image_files = [f for f in os.listdir(input_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.tif', '.tiff'))]

for img_file in image_files:
    img_path = os.path.join(input_folder, img_file)
    img = read_image(img_path)  # Read image with TIFF support

    if img is None:
        print(f"Could not read {img_file}, skipping...")
        continue

    # Get original image dimensions (height, width)
    height, width = img.shape  
    print(f"Processing {img_file} - Original Resolution: {width}x{height} pixels")

    # Step 1: Enhance Image
    enhanced_img = enhance_image(img)

    # Step 2: Add Gaussian Noise
    noisy_img = add_gaussian_noise(img)

    # Step 3: Remove Noise using different filters
    arithmetic_filtered = arithmetic_mean_filter(noisy_img)

    geometric_filtered = geometric_mean_filter(noisy_img)

    gaussian_filtered = gaussian_filter(noisy_img)

    # Save results
    cv2.imwrite(os.path.join(output_folder, f"enhanced_{img_file}"), enhanced_img)
    cv2.imwrite(os.path.join(output_folder, f"noisy_{img_file}"), noisy_img)
    cv2.imwrite(os.path.join(output_folder, f"arithmetic_filtered_{img_file}"), arithmetic_filtered)
    cv2.imwrite(os.path.join(output_folder, f"geometric_filtered_{img_file}"), geometric_filtered)
    cv2.imwrite(os.path.join(output_folder, f"gaussian_filtered_{img_file}"), gaussian_filtered)

    # Display results
    plt.figure(figsize=(15, 8))

    images = [img, enhanced_img, noisy_img, arithmetic_filtered, geometric_filtered, gaussian_filtered]
    titles = ["Original (Grayscale)", "Enhanced", "Noisy (Gaussian)", "Arithmetic Mean", "Geometric Mean", "Gaussian Filter"]

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(images[i], cmap='gray')  # Use grayscale colormap
        plt.title(titles[i])
        plt.axis("off")

    plt.show()

print(f"Processed images saved in {output_folder}")
