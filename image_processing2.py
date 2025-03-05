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

# Function to add Salt & Pepper noise
def add_salt_and_pepper_noise(img, salt_prob=0.02, pepper_prob=0.02):
    noisy_img = img.copy()
    total_pixels = img.size

    # Add salt (white) noise
    num_salt = int(total_pixels * salt_prob)
    salt_coords = [np.random.randint(0, i, num_salt) for i in img.shape]
    noisy_img[salt_coords[0], salt_coords[1]] = 255

    # Add pepper (black) noise
    num_pepper = int(total_pixels * pepper_prob)
    pepper_coords = [np.random.randint(0, i, num_pepper) for i in img.shape]
    noisy_img[pepper_coords[0], pepper_coords[1]] = 0

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

# Function to apply Harmonic Mean Filter
def harmonic_mean_filter(img, kernel_size=5):
    img = img.astype(np.float32) + 1e-9  # Avoid division by zero
    inv_img = 1.0 / img
    mean_inv = cv2.blur(inv_img, (kernel_size, kernel_size))
    harmonic_mean = 1.0 / mean_inv
    return np.clip(harmonic_mean, 0, 255).astype(np.uint8)

# Function to plot histograms
def plot_histogram(image, title, subplot_position):
    plt.subplot(2, 4, subplot_position)
    plt.hist(image.ravel(), bins=256, range=[0, 256], color='black', alpha=0.75)
    plt.title(title)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')

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

    # Step 1: Enhance Image
    enhanced_img = enhance_image(img)

    # Step 2: Add Gaussian and Salt & Pepper Noise
    gaussian_noisy = add_gaussian_noise(img)
    salt_pepper_noisy = add_salt_and_pepper_noise(img)

    # Step 3: Remove Noise using different filters
    arithmetic_filtered = arithmetic_mean_filter(gaussian_noisy)
    geometric_filtered = geometric_mean_filter(gaussian_noisy)
    harmonic_filtered = harmonic_mean_filter(gaussian_noisy)

    # Save results
    cv2.imwrite(os.path.join(output_folder, f"enhanced_{img_file}"), enhanced_img)
    cv2.imwrite(os.path.join(output_folder, f"gaussian_noisy_{img_file}"), gaussian_noisy)
    cv2.imwrite(os.path.join(output_folder, f"salt_pepper_noisy_{img_file}"), salt_pepper_noisy)

    cv2.imwrite(os.path.join(output_folder, f"arithmetic_filtered_{img_file}"), arithmetic_filtered)
    cv2.imwrite(os.path.join(output_folder, f"geometric_filtered_{img_file}"), geometric_filtered)
    cv2.imwrite(os.path.join(output_folder, f"harmonic_filtered_{img_file}"), harmonic_filtered)

    # Display images
    plt.figure(figsize=(15, 10))
    images = [img, enhanced_img, gaussian_noisy, salt_pepper_noisy, arithmetic_filtered, geometric_filtered, harmonic_filtered]
    titles = ["Original", "Enhanced", "Gaussian Noise", "Salt & Pepper Noise", 
              "Denoised (Arithmetic)", "Denoised (Geometric)", "Denoised (Harmonic)"]

    for i in range(7):
        plt.subplot(2, 4, i + 1)
        plt.imshow(images[i], cmap='gray')  # Use grayscale colormap
        plt.title(titles[i])
        plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Display histograms
    plt.figure(figsize=(15, 8))
    plot_histogram(img, "Histogram (Original)", 1)
    plot_histogram(enhanced_img, "Histogram (Enhanced)", 2)
    plot_histogram(gaussian_noisy, "Histogram (Gaussian Noise)", 3)
    plot_histogram(salt_pepper_noisy, "Histogram (Salt & Pepper Noise)", 4)
    plot_histogram(arithmetic_filtered, "Histogram (Denoised - Arithmetic)", 5)
    plot_histogram(geometric_filtered, "Histogram (Denoised - Geometric)", 6)
    plot_histogram(harmonic_filtered, "Histogram (Denoised - Harmonic)", 7)

    plt.tight_layout()
    plt.show()

print(f"Processed images saved in {output_folder}")
