import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('calorie_prediction_model.joblib')

st.title('Calorie Burn Prediction App')
st.write('Enter the details below to predict calorie burn.')

# Input fields for features
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.slider('Age', 15, 80, 30)
height = st.slider('Height (cm)', 120, 220, 170)
weight = st.slider('Weight (kg)', 30, 150, 70)
duration = st.slider('Duration (minutes)', 1, 30, 15)
heart_rate = st.slider('Heart Rate', 60, 120, 90)
body_temp = st.slider('Body Temperature (°C)', 35.0, 42.0, 37.0, 0.1)

# Convert gender to numerical (0 for Male, 1 for Female)
gender_encoded = 0 if gender == 'Male' else 1

# Create a DataFrame for prediction
input_data = pd.DataFrame([[gender_encoded, age, height, weight, duration, heart_rate, body_temp]],
                           columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'])

if st.button('Predict Calories'):
    prediction = model.predict(input_data)[0]
    st.success(f'Predicted Calories Burned: {prediction:.2f}')
