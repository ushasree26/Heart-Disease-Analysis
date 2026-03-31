from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load trained ML model
model = joblib.load("heart_model.pkl")


# Landing Page
@app.route('/')
def index():
    return render_template('index.html')


# Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# About Page
@app.route('/about')
def about():
    return render_template('about.html')


# Story Page
@app.route('/story')
def story():
    return render_template('story.html')


# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Prediction Page
@app.route('/predict')
def predict_page():
    return render_template('predict.html')




# ❤️ Heart Disease Prediction
@app.route('/predict', methods=['POST'])
def predict():

    data = request.form

    features = [
        float(data['BMI']),
        int(data['Smoking']),
        int(data['AlcoholDrinking']),
        int(data['Stroke']),
        int(data['PhysicalHealth']),
        int(data['MentalHealth']),
        int(data['DiffWalking']),
        int(data['Sex']),
        int(data['AgeCategory']),
        int(data['Race']),
        int(data['Diabetic']),
        int(data['PhysicalActivity']),
        int(data['GenHealth']),
        int(data['SleepTime']),
        int(data['Asthma']),
        int(data['KidneyDisease']),
        int(data['SkinCancer'])
    ]

    prediction = model.predict([features])

    if prediction[0] == 1:
        result = "High Risk of Heart Disease"
    else:
        result = "Low Risk of Heart Disease"

    return render_template("result.html", prediction=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)