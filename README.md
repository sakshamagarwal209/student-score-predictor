# Student Score Predictor 📊

A beginner-friendly end-to-end Machine Learning project that predicts a student’s exam score based on the number of hours studied.

---

## 🔍 Overview

This project demonstrates the complete workflow of a supervised machine learning application:
- Loading and exploring data
- Training a Linear Regression model
- Saving and loading the trained model
- Deploying the model using an interactive Streamlit web app

The goal is to understand ML fundamentals while building something practical and presentable.

---

## 🚀 Features

- Predict exam scores using:
  - A slider input
  - A numeric input box
- Real-time predictions using a trained ML model
- Persistent prediction history
- Interactive table of past predictions
- Line chart visualization of Hours Studied vs Predicted Score
- Download prediction history as a CSV file
- Clear prediction history with one click

---

## 🛠 Tech Stack

- **Python**
- **scikit-learn** (Linear Regression)
- **pandas**
- **NumPy**
- **Streamlit**

---

## 📂 Project Structure

student-score-predictor/
├── app.py # Streamlit web application
├── train.py # Model training script
├── predict.py # Standalone prediction script
├── test_predictions.py # Model testing & validation
├── requirements.txt # Project dependencies
├── README.md
├── .gitignore
│
├── data/
│ └── student_scores.csv # Dataset
│
└── model/
└── model.pkl # Trained ML model

---

## ▶️ How to Run Locally

pip install -r requirements.txt
python train.py
streamlit run app.py

## 🧪 Model Testing

The test_predictions.py script validates the trained model by comparing actual scores with predicted values from the dataset.

## 🎯 Learning Outcomes

Understanding supervised learning and Linear Regression

Building and evaluating ML models using scikit-learn

Model persistence using pickle

Deploying ML models using Streamlit

Version control using Git and GitHub