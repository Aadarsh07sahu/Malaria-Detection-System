# 🦠 Malaria Detection System using Deep Learning

A web-based **Malaria Detection System** that uses a **Deep Learning Convolutional Neural Network (CNN)** model to detect malaria parasites from microscopic blood cell images.

The application allows users to upload a blood cell image and predicts whether the cell is **Parasitized (infected)** or **Uninfected (healthy)**.

This project combines **Deep Learning, Image Processing, and Web Development** to build a simple and effective malaria detection tool.

---

## 📖 Project Description

Malaria remains one of the world's deadliest diseases, affecting millions of people annually, particularly in tropical and subtropical regions. Early and accurate detection of malaria parasites in blood samples is crucial for effective treatment and disease management. Traditional microscopic examination of blood smears is time-consuming, labor-intensive, and requires expert pathologists, which are often unavailable in remote areas.

This project leverages **Deep Learning**, specifically **Convolutional Neural Networks (CNNs)**, to automate malaria detection from microscopic blood cell images. The system provides a **fast, accurate, and scalable solution** that can assist medical professionals in diagnosing malaria infections.

A **Custom CNN model** was developed and trained to classify microscopic blood cell images as **Parasitized** or **Uninfected**. The model achieved **98.99% validation accuracy** with an **ROC-AUC score of 0.9995**, demonstrating strong predictive performance for malaria detection.

The project implements a **complete end-to-end pipeline**, including dataset preprocessing, model training, evaluation, and deployment through a **Flask web application**. Users can upload blood cell images through the web interface and receive predictions within **3–4 seconds** with confidence scores.

This system can assist healthcare workers in **resource-limited regions** where expert pathologists may not always be available, helping enable **early malaria detection and timely treatment**.

---

## ✨ Features

* Upload microscopic blood cell images for malaria detection
* Deep Learning model for accurate prediction
* Classifies images as **Parasitized** or **Uninfected**
* Simple and user-friendly web interface
* Fast prediction using trained CNN model
* Login and Signup functionality

---

## 🛠 Technologies Used

### Programming Language

* Python

### Web Framework

* Flask

### Deep Learning

* TensorFlow
* Keras

### Image Processing

* OpenCV
* NumPy
* Pillow (PIL)

### Frontend

* HTML
* CSS

---

## 📂 Project Structure

```
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
```

---

## ⚙️ How the System Works

1. User opens the web application.
2. User signs up or logs into the system.
3. User uploads a microscopic blood cell image.
4. The image is stored in the **uploads** folder.
5. The image is preprocessed using **OpenCV and NumPy**.
6. The trained **CNN model** analyzes the image.
7. The model predicts whether the cell is infected or not.
8. The result is displayed on the **result page**.

---

## 🧠 Deep Learning Model

The system uses a **Convolutional Neural Network (CNN)** model trained on malaria cell images.

The model classifies images into two categories:

* **Parasitized → Malaria infected cell**
* **Uninfected → Healthy blood cell**

The trained model file used in this project:

```
model.keras
```

---

## 📊 Dataset

The model is trained using the **Malaria Cell Images Dataset** containing microscopic blood cell images.

Dataset classes:

* Parasitized
* Uninfected

---

## 🚀 Installation and Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/Malaria-Detection-System.git
```

### 2️⃣ Navigate to project folder

```
cd Malaria-Detection-System
```

### 3️⃣ Create virtual environment

```
python -m venv venv
```

### 4️⃣ Activate virtual environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 5️⃣ Install required libraries

```
pip install flask tensorflow keras numpy opencv-python pillow
```

### 6️⃣ Run the application

```
python app.py
```

---

## 📥 Download Trained Model

Due to large file size, the trained model is not included in this repository.

Download the trained model from Google Drive:

https://drive.google.com/file/d/1MtOBD-q-i2cic1EdGbIYF0iBRRMBjeMR/view?usp=sharing

---


⭐ If you found this project helpful, consider giving it a **star on GitHub**.
