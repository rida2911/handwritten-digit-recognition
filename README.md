# Handwritten Digit Recognition

A web application that predicts handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. The model is deployed using Streamlit for real-time interaction.

---

## Features

- Upload and process images of handwritten digits
- Preprocessing: resizing, grayscale conversion, inversion, thresholding
- Real-time digit prediction with confidence score
- Clean, minimal interface with responsive output

---

## Model Architecture

The CNN model was trained on the MNIST dataset and consists of:

- Convolutional Layers (ReLU activation)
- Max Pooling Layer
- Dense Fully Connected Layer
- Output Layer with Softmax activation (10 classes: digits 0–9)

---

## Tech Stack

- **Language:** Python 
- **Frontend:** Streamlit
- **Backend:** TensorFlow, Keras
- **Image Processing:** OpenCV, Pillow

---

## How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/rida2911/handwritten-digit-recognition.git
   cd handwritten-digit-recognition

