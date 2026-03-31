import joblib
import pandas as pd

model = joblib.load("heart_model.pkl")

# column names from dataset
columns = [
"BMI","Smoking","AlcoholDrinking","Stroke","PhysicalHealth",
"MentalHealth","DiffWalking","Sex","AgeCategory","Race",
"Diabetic","PhysicalActivity","GenHealth","SleepTime",
"Asthma","KidneyDisease","SkinCancer"
]

# sample patient data
data = pd.DataFrame([[28,1,0,0,5,5,0,1,8,3,0,1,3,7,0,0,0]], columns=columns)

prediction = model.predict(data)

if prediction[0] == 1:
    print("High Risk of Heart Disease")
else:
    print("Low Risk of Heart Disease")