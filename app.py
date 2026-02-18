import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image

# -------------------------------
# Load Trained Model
# -------------------------------
model = load_model("brain_tumor_model.h5")

# Class names (must match training folder names exactly)
labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("Brain Tumor Detection using CNN")
st.write("Upload an MRI image to predict the tumor type.")

uploaded_file = st.file_uploader("Choose an MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    
    # Convert uploaded file to RGB
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to numpy
    img = np.array(image)

    # Resize
    img = cv2.resize(img, (128, 128))

    # Normalize
    img = img / 255.0

    # Add batch dimension properly
    img = np.expand_dims(img, axis=0)


    # Prediction
    prediction = model.predict(img)

    pred_class = np.argmax(prediction)
    predicted_label = labels[pred_class]
    confidence = np.max(prediction) * 100

    st.subheader("Prediction Result:")
    st.success(f"Predicted Tumor Type: {predicted_label}")
    st.info(f"Confidence: {confidence:.2f}%")
