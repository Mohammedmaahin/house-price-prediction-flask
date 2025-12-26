# 🏠 House Price Prediction Web Application

## 📌 Overview
This project is an end-to-end Machine Learning web application that predicts house prices based on user-provided inputs such as **area**, **number of bedrooms**, and **age of the house**.  
A **Linear Regression** model is trained on housing data and deployed using a **Flask API** with a clean **HTML/CSS frontend** for real-time predictions.

---

## 🚀 Features
- User-friendly web interface
- Predicts house prices based on multiple features
- Trained Machine Learning model integrated with Flask backend
- Real-time predictions through a web form
- Clean and responsive UI using HTML & CSS

---

## 🧠 Machine Learning Pipeline
- Data loading and preprocessing
- Handling missing values using median imputation
- Feature scaling using `StandardScaler`
- Multivariate Linear Regression model
- Model evaluation using **RMSE** and **R² Score**
- Model serialization using **pickle**

---

## 📊 Model Performance
- **RMSE:** ~21,126  
- **R² Score:** ~0.95  

> *Note: Due to the limited size of the dataset, the model was trained and evaluated on the full dataset to demonstrate the complete end-to-end machine learning workflow.*

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn  
- **Backend:** Flask  
- **Frontend:** HTML, CSS  
- **Tools:** Git, GitHub  

---

## 📁 Project Structure
house-price-prediction-flask/
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── templates/
│ └── index.html
├── static/
│ └── style.css
└── README.md


---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Mohammedmaahin/house-price-prediction-flask.git
cd house-price-prediction-flask

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run the Flask App
python app.py

### 4️⃣ Open in Browser
http://127.0.0.1:5000/
