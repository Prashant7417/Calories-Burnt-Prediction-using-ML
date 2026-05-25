# Calories-Burnt-Prediction-using-ML

This project develops a machine learning model to predict calorie expenditure during exercise, based on various physiological and activity-related parameters. The model is deployed as an interactive web application using Streamlit, allowing users to input their details and get an estimated calorie burn.


Live StreamLit: https://calories-burnt-prediction-using-ml-5jgcdkxbsxzuyns2hyjappc.streamlit.app/

# Project Overview:
Understanding calorie expenditure is crucial for fitness tracking and health management. This project aims to build a predictive model that estimates the number of calories burned based on factors like gender, age, height, weight, exercise duration, heart rate, and body temperature. The trained model is then exposed via a user-friendly Streamlit web application.

Dataset :
The project utilizes two datasets:

calories.csv : Contains User_ID and Calories burned.

exercise.csv : Contains User_ID and various features such as Gender, Age, Height, Weight, Duration, Heart_Rate, and Body_Temp.

These datasets were merged to create a comprehensive dataset for training the model. Data preprocessing included handling categorical features (Gender) by converting them to numerical representations.

# Model Training :
An XGBoost Regressor model was chosen for its robust performance in regression tasks. The dataset was split into training and testing sets, and the model was trained to predict the Calories burned based on the input features. The model's performance was evaluated using Mean Absolute Error (MAE).

The trained machine learning model is deployed as a web application using Streamlit. Users can interact with sliders and selectors to input their details, and the application will provide a real-time prediction of calorie burn. This makes the model accessible and easy to use for anyone interested in fitness tracking.
