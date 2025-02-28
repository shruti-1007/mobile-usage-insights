import streamlit as st
import joblib
import pandas as pd
# Data visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Function to scale input data manually
def min_max_scale(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0  # Prevent division by zero
# Function to reverse scaling (inverse scaling)
def inverse_min_max_scale(scaled_value, min_val, max_val):
    return (scaled_value * (max_val - min_val)) + min_val

with open('../data/min_max_values.json', 'r') as f:
    min_max_values = json.load(f)


# Load the trained model
model = joblib.load('../models/battery_drain_model.pkl')

# Title of the app
st.title('Battery Drain Prediction')

# Input fields for user data (screen time, app usage, and data consumption)
screen_on_time = st.number_input('Enter Screen On Time (hours per day)', min_value=0.0, max_value=24.0, value=5.0)
app_usage_time = st.number_input('Enter App Usage Time (minutes per day)', min_value=0, value=120)
data_usage = st.number_input('Enter Data Usage (MB per day)', min_value=0, value=500)
number_of_apps = st.number_input('Enter Number of Apps', min_value=0, value=30)
os_type = st.selectbox('Select OS Type', ['Android', 'iOS'])
os_type = 1 if os_type == 'iOS' else 0

input_data_scaled = [
       
    min_max_scale(screen_on_time, min_max_values['Screen On Time (hours/day)']['min'], min_max_values['Screen On Time (hours/day)']['max']),
    min_max_scale(app_usage_time, min_max_values['App Usage Time (min/day)']['min'], min_max_values['App Usage Time (min/day)']['max']),
    min_max_scale(data_usage, min_max_values['Data Usage (MB/day)']['min'], min_max_values['Data Usage (MB/day)']['max']),
    min_max_scale(number_of_apps, min_max_values['Number of Apps Installed']['min'], min_max_values['Number of Apps Installed']['max']),
   os_type]


# Predict button
if st.button('Predict Battery Drain'):
    # Prepare the input data as a DataFrame (model expects a 2D array)
    input_data = pd.DataFrame([input_data_scaled],
                              columns=['Screen On Time (hours/day)', 'App Usage Time (min/day)', 'Data Usage (MB/day)', 'Number of Apps Installed', 'Operating System'])
    
    # Make a prediction
    predicted_battery_drain = model.predict(input_data)
    predicted_battery_drain = inverse_min_max_scale(predicted_battery_drain[0], min_max_values['Battery Drain (mAh/day)']['min'], min_max_values['Battery Drain (mAh/day)']['max'])


    # Show the result
    st.write(f"Predicted Battery Drain: {predicted_battery_drain:.2f} mAh")

