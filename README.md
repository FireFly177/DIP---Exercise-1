# Digital Image Processing - Exercise 1: Image enhance, Noise Addition & Removal


---

## 📌 Setup Guide

### 1️⃣ **Create a Virtual Environment**
Before running the project, create a virtual environment to manage dependencies:
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

### 2️⃣ **Install Dependencies**
Install all required Python packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### 3️⃣ **Prepare Input Images**
Place your images inside the `images/` folder.

---

### 4️⃣ **Run the Script**
Run the Python script to process images:
```bash
python process_images.py
```

---

### 5️⃣ **Output Files**
Processed images will be saved in the `processed_images/` folder.

Each image will have:
- `enhanced_<filename>.jpg` → Histogram Equalization applied.
- `noisy_<filename>.jpg` → Gaussian noise added.
- `arithmetic_filtered_<filename>.jpg` → Denoised with Arithmetic Mean Filter.
- `geometric_filtered_<filename>.jpg` → Denoised with Geometric Mean Filter.
- `gaussian_filtered_<filename>.jpg` → Denoised with Gaussian Filter.

---

## 🛠 Dependencies
All dependencies are installed automatically using `requirements.txt`.

---

## ⚡ Example Console Output
```bash
Processing img1.jpg - Original Resolution: 540x360 pixels
Resized img1.jpg to 1280x720 pixels
Enhance img1.jpg Resolution: 1280x720 pixels
Noisy img1.jpg - Resolution: 1280x720 pixels
Filtered img1.jpg - Resolution: 1280x720 pixels
Filtered img1.jpg - Resolution: 1280x720 pixels
Filtered img1.jpg - Resolution: 1280x720 pixels
Processing img2.jpg - Original Resolution: 6067x3467 pixels
Resized img2.jpg to 1280x720 pixels
Enhance img2.jpg Resolution: 1280x720 pixels
Noisy img2.jpg - Resolution: 1280x720 pixels
Filtered img2.jpg - Resolution: 1280x720 pixels
Filtered img2.jpg - Resolution: 1280x720 pixels
Filtered img2.jpg - Resolution: 1280x720 pixels
Processing img3.jpg - Original Resolution: 5250x3500 pixels
Resized img3.jpg to 1280x720 pixels
Enhance img3.jpg Resolution: 1280x720 pixels
Noisy img3.jpg - Resolution: 1280x720 pixels
Filtered img3.jpg - Resolution: 1280x720 pixels
Filtered img3.jpg - Resolution: 1280x720 pixels
Filtered img3.jpg - Resolution: 1280x720 pixels
Processing img4.jpg - Original Resolution: 3452x5178 pixels
Resized img4.jpg to 1280x720 pixels
Enhance img4.jpg Resolution: 1280x720 pixels
Noisy img4.jpg - Resolution: 1280x720 pixels
Filtered img4.jpg - Resolution: 1280x720 pixels
Filtered img4.jpg - Resolution: 1280x720 pixels
Filtered img4.jpg - Resolution: 1280x720 pixels
Processing img5.jpg - Original Resolution: 6000x4000 pixels
Resized img5.jpg to 1280x720 pixels
Enhance img5.jpg Resolution: 1280x720 pixels
Noisy img5.jpg - Resolution: 1280x720 pixels
Filtered img5.jpg - Resolution: 1280x720 pixels
Filtered img5.jpg - Resolution: 1280x720 pixels
Filtered img5.jpg - Resolution: 1280x720 pixels
Processed images saved in processed_images
```

---
