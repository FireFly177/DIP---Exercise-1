# Digital Image Processing - Exercise 1: Image Enhancement, Noise Addition & Removal

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
Place your images inside the `images/` folder. There are 5 sample images in the `/images` folder.

---

### 4️⃣ **Run the Script**
Run the Python script to process images:
```bash
python image_processing2.py
```

---

### 5️⃣ **Output Files**
Processed images will be saved in the `processed_images/` folder.

Each image will have:
- `enhanced_<filename>.jpg` → Histogram Equalization applied.
- `gaussian_noisy_<filename>.jpg` → Gaussian noise added.
- `salt_pepper_noisy_<filename>.jpg` → Salt & Pepper noise added.
- `arithmetic_filtered_<filename>.jpg` → Denoised with Arithmetic Mean Filter.
- `geometric_filtered_<filename>.jpg` → Denoised with Geometric Mean Filter.
- `harmonic_filtered_<filename>.jpg` → Denoised with Harmonic Mean Filter.

---

## 🛠 Dependencies
All dependencies are installed automatically using `requirements.txt`.

---


## ⚡ Example Output
![Example output](./resultREADME/result1.png)
![Example output](./resultREADME/result2.png)
