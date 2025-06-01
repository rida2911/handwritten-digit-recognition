# Handwritten Digit Recognition

This project is a web application for recognizing handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. It leverages TensorFlow and Keras for model training and Streamlit for deployment.

---

## Key Features

- Upload handwritten digit images via a simple web UI
- Real-time prediction with confidence score
- Preprocessing pipeline: resizing, grayscale conversion, inversion, and thresholding
- Trained on MNIST dataset with >99% accuracy
- Clean frontend built using Streamlit

---

## Neural Network Architecture

The CNN model consists of:

- 2 Convolutional layers with ReLU activation
- 1 MaxPooling layer to reduce dimensionality
- 1 Fully connected Dense hidden layer
- 1 Output layer with Softmax activation for 10-class classification (digits 0–9)

---

## Dataset: MNIST

- 60,000 training images
- 10,000 test images
- 28x28 grayscale images, centered, normalized
- Widely used benchmark for digit recognition

---

## Installation & Setup

### Prerequisites

- Python 3.10
- pip

### Steps

1. Clone the repository:

git clone https://github.com/yourusername/handwritten-digit-recognition.git
cd handwritten-digit-recognition

Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate   # On Windows



