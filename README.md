# 🧠 Brain Tumor Detection using CNN

## 📌 Overview

Brain Tumor Detection using CNN is a deep learning-based medical image classification system designed to identify different types of brain tumors from MRI scans. The application utilizes a Convolutional Neural Network (CNN) trained on MRI images to classify brain scans into four categories:

* Glioma Tumor
* Meningioma Tumor
* Pituitary Tumor
* No Tumor

The trained model is integrated with a Streamlit web application, allowing users to upload MRI images and receive instant predictions along with confidence scores.

---

## 🎯 Problem Statement

Early detection of brain tumors is critical for effective treatment and patient care. Manual analysis of MRI scans can be time-consuming and requires expert radiologists.

This project aims to assist in preliminary tumor classification by leveraging deep learning techniques to automatically analyze MRI images and predict tumor types.

---

## ✨ Features

### 🖼 MRI Image Upload

* Upload MRI scans in JPG, JPEG, or PNG format.
* Simple and user-friendly interface built with Streamlit.

### 🧠 CNN-Based Classification

* Uses a trained Convolutional Neural Network model.
* Automatically predicts the tumor category.

### 📊 Confidence Score

* Displays prediction confidence percentage.
* Helps users understand model certainty.

### ⚡ Real-Time Prediction

* Instant image processing and classification.
* Interactive web-based experience.

---

## 🏗️ System Workflow

```text
User Uploads MRI Image
            │
            ▼
Image Preprocessing
(Resize + Normalize)
            │
            ▼
CNN Model
(brain_tumor_model.h5)
            │
            ▼
Probability Scores
            │
            ▼
Predicted Class
            │
            ▼
Display Result + Confidence
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Deep Learning

* TensorFlow
* Keras

### Computer Vision

* OpenCV
* NumPy

### Web Application

* Streamlit

### Image Processing

* Pillow (PIL)

---

## 🧠 Model Classes

The CNN model classifies MRI scans into the following categories:

| Class      | Description                            |
| ---------- | -------------------------------------- |
| Glioma     | Tumor originating from glial cells     |
| Meningioma | Tumor arising from the meninges        |
| Pituitary  | Tumor affecting the pituitary gland    |
| No Tumor   | Normal MRI scan with no detected tumor |

---

## ⚙️ Preprocessing Pipeline

Before prediction, each uploaded MRI image undergoes the following preprocessing steps:

1. Convert image to RGB format
2. Resize image to 128 × 128 pixels
3. Normalize pixel values between 0 and 1
4. Add batch dimension for CNN input
5. Pass image to trained model

---

## 🚀 How It Works

### Step 1

User uploads an MRI image through the Streamlit interface.

### Step 2

The image is converted into a numerical format suitable for deep learning.

### Step 3

The CNN model analyzes visual features from the MRI scan.

### Step 4

The model generates probability scores for each tumor category.

### Step 5

The class with the highest probability is selected as the final prediction.

### Step 6

The predicted tumor type and confidence score are displayed to the user.

---

## 📊 Sample Output

```text
Predicted Tumor Type: Glioma

Confidence: 97.85%
```

---

## 💡 Applications

* Medical image classification
* Brain tumor screening assistance
* Healthcare AI research
* Deep learning in medical imaging
* Educational demonstrations of CNN models

---

## 🔮 Future Enhancements

* Support for DICOM medical images
* Grad-CAM visualization for model explainability
* Multi-image batch prediction
* Cloud deployment
* Model performance dashboard
* Patient report generation
* Integration with hospital information systems

---

## 👨‍💻 Author

**Chinmaya A S**

Aspiring AI/ML Engineer | Data Science Enthusiast | Deep Learning Practitioner

GitHub: https://github.com/chinmaya-sajeevan

LinkedIn: https://www.linkedin.com/in/chinmaya-a-s
