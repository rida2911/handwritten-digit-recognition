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

### About MNIST dataset:
The MNIST database (Modified National Institute of Standards and Technology database) of handwritten digits consists of a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. Additionally, the black and white images from NIST were size-normalized and centered to fit into a 28x28 pixel bounding box and anti-aliased, which introduced grayscale levels.

---

## Neural Network Architecture

This CNN model follows a **feedforward architecture** where layers are stacked sequentially:

- **Input Layer**: Accepts 28x28 grayscale images
- **Convolutional Layers**: Extract spatial features using filters and ReLU activation
- **MaxPooling Layer**: Downsamples feature maps to reduce dimensionality
- **Dense Layer**: Fully connected for higher-level reasoning
- **Output Layer**: Softmax activation classifies input into one of 10 digits (0–9)

---
## Prerequisites

- Python 3.10
- TensorFlow 2.x
- NumPy
- OpenCV
- Pillow
- Streamlit
---


## Getting Started

How to use
```    
git clone https://github.com/rida2911/handwritten-digit-recognition.git
cd Handwritten-Digit-Recognition
```
Install dependencies
```
pip install -r requirements.txt
```
Run the Application

```
streamlit run app.py
```

## Result:
Following image is the prediction of the model.
![result](https://github.com/user-attachments/assets/8f4fed1a-0abd-49b1-be18-cfc1eaac8a69)









