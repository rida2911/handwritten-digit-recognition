import streamlit as st
import numpy as np
import cv2
from PIL import Image
from tensorflow.keras.models import load_model

# Load trained CNN model
model = load_model("tf-cnn-model.h5", compile=False)

# App title
st.title("Handwritten Digit Recognition")

st.markdown(
    """
    Upload an image of a handwritten digit (0–9).  
    The model will predict the digit using a Convolutional Neural Network trained on the MNIST dataset.
    """
)

# Upload image
uploaded_file = st.file_uploader("Upload an image (28x28 or similar)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('L')  # Convert to grayscale
    st.image(image, caption="Uploaded Image", width=150)

    # Resize and preprocess
    image = image.resize((28, 28))
    image_np = np.array(image)
    image_np = 255 - image_np  # Invert colors: black background
    image_np = image_np / 255.0  # Normalize
    image_np = image_np.reshape(1, 28, 28, 1)

    # Predict
    prediction = model.predict(image_np)
    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    # Show prediction
    st.subheader(f"Predicted Digit: {predicted_class}")
    st.text(f"Confidence: {confidence:.2f}%")