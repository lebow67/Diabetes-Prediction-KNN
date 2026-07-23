# Diabetes-Prediction-KNN
Diabetes prediction using K-Nearest Neighbors (KNN) with a Gradio web application.

# 🩺 Diabetes Prediction using K-Nearest Neighbors (KNN)

A Machine Learning project that predicts whether a patient is diabetic based on medical measurements using the **K-Nearest Neighbors (KNN)** algorithm. The project includes data preprocessing, exploratory data analysis, model training, evaluation, and an interactive Gradio web application for real-time predictions.

---

## 📌 Project Highlights

- 📊 Data Cleaning & Preprocessing
- 📈 Exploratory Data Analysis (EDA)
- 🤖 Machine Learning Model using KNN
- 🎯 Model Evaluation
- 💾 Model Serialization using Joblib
- 🌐 Interactive Gradio Web Application

---

## 📂 Project Structure

```text
Diabetes-Prediction-KNN/
│
├── app.py                     # Gradio web application
├── diabetes_prediction.ipynb  # Jupyter notebook
├── diabetes.csv               # Dataset
├── diabetes_model.pkl         # Trained KNN model
├── scaler.pkl                 # StandardScaler
├── columns.pkl                # Feature names
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

This project uses the **Pima Indians Diabetes Dataset** to predict whether a patient has diabetes based on several medical attributes.

### Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target

- **0 → Not Diabetic**
- **1 → Diabetic**

---

## 🧹 Data Preprocessing

Before training the model, the dataset was cleaned and prepared.

### Handling Invalid Values

The following columns contained impossible zero values:

- Glucose
- Blood Pressure
- BMI

These values were replaced using the **median**.

For the following columns:

- Skin Thickness
- Insulin

Missing values were filled using the **median within each Outcome group**, helping preserve the distribution of diabetic and non-diabetic patients.

### Feature Scaling

All features were standardized using **StandardScaler** before training the model.

---

## 🤖 Machine Learning Model

**Algorithm Used**

- K-Nearest Neighbors (KNN)

**Libraries Used**

- Scikit-learn
- Pandas
- NumPy

---

## 📈 Model Evaluation

The model was evaluated using:

- Accuracy Score
- Confusion Matrix
- Classification Report

---

## 🌐 Gradio Web Application

The application allows users to:

- Enter patient medical information
- Predict whether the patient is diabetic
- View the prediction confidence score

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Gradio

---

## ▶️ Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/lebow67/Diabetes-Prediction-KNN.git
```

Navigate to the project directory:

```bash
cd Diabetes-Prediction-KNN
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Gradio application:

```bash
python app.py
```

---

## 📌 Future Improvements

- 🚀 Deploy the application on Render
- 🎨 Improve the Gradio interface with custom CSS
- 📊 Compare KNN with other machine learning algorithms
- ⚙️ Perform hyperparameter tuning
- 📈 Add additional visualizations and model insights

---

## 👨‍💻 Author

**Pranil Kumar Walwandre**

- **GitHub:** https://github.com/lebow67
- **LinkedIn:** https://www.linkedin.com/in/pranil-kumar-walwandre-b1ab88423/

---

## ⭐ Support

If you found this project useful, consider giving this repository a **⭐ Star**.
