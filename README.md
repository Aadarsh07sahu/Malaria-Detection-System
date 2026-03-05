# Malaria-Detection-System
A web-based Malaria Detection System that uses a Deep Learning CNN model to identify malaria parasites from microscopic blood cell images. Built using TensorFlow, Keras, OpenCV and Flask.
A web-based Malaria Detection System that uses a Deep Learning Convolutional Neural Network (CNN) model to detect malaria parasites from microscopic blood cell images.

The system allows users to upload a blood cell image and predicts whether the cell is Parasitized (infected) or Uninfected (healthy).

This project combines Deep Learning, Image Processing, and Web Development to build a simple and effective malaria detection tool.

📌 Features

Upload microscopic blood cell images

Deep Learning based malaria detection

Classifies images into Parasitized and Uninfected

Simple web interface

Fast and automatic prediction

Login and Signup functionality

🛠 Technologies Used
Programming Language

Python

Web Framework

Flask

Deep Learning

TensorFlow

Keras

Image Processing

OpenCV

NumPy

Pillow (PIL)

Frontend

HTML

CSS

📂 Project Structure
Malaria_D_S
│
├── static
│   └── css
│       └── style.css
│
├── templates
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   └── result.html
│
├── uploads
│   └── (uploaded images)
│
├── app.py
├── model.keras
└── venv
⚙️ How the System Works

User opens the web application.

User signs up or logs into the system.

User uploads a microscopic blood cell image.

The image is stored in the uploads folder.

The image is preprocessed using OpenCV and NumPy.

The trained CNN model analyzes the image.

The model predicts whether the cell is infected or not.

The prediction result is displayed on the result page.

🧠 Deep Learning Model

The system uses a Convolutional Neural Network (CNN) model trained on malaria cell images.

The model classifies images into two categories:

Parasitized → Malaria infected cell

Uninfected → Healthy blood cell

The trained model file used in this project:

model.keras
📊 Dataset

The model is trained using the Malaria Cell Images Dataset which contains thousands of microscopic blood cell images.

Dataset classes:

Parasitized

Uninfected
## Download Trained Model

Due to large file size, the trained model is not included in this repository.

Download the trained model from Google Drive:

https://drive.google.com/file/d/1MtOBD-q-i2cic1EdGbIYF0iBRRMBjeMR/view?usp=sharing
