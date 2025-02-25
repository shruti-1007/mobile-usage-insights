import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('C:/Users/Acer/Desktop/Data Science Project/models/battery_drain_model.pkl')

# Title of the app
st.title('Battery Drain Prediction')

# Input fields for user data (screen time, app usage, and data consumption)
screen_on_time = st.number_input('Enter Screen On Time (hours per day)', min_value=0.0, max_value=24.0, value=5.0)
app_usage_time = st.number_input('Enter App Usage Time (minutes per day)', min_value=0, value=120)
data_usage = st.number_input('Enter Data Usage (MB per day)', min_value=0, value=500)
number_of_apps = st.number_input('Enter Number of Apps', min_value=0, value=30)
os_type = st.selectbox('Select OS Type', ['Android', 'iOS'])
os_type = 1 if os_type == 'iOS' else 0

# Predict button
if st.button('Predict Battery Drain'):
    # Prepare the input data as a DataFrame (model expects a 2D array)
    input_data = pd.DataFrame([[screen_on_time, app_usage_time, data_usage, number_of_apps, os_type]],
                              columns=['Screen On Time (hours/day)', 'App Usage Time (min/day)', 'Data Usage (MB/day)', 'Number of Apps Installed', 'Operating System'])

    # Make a prediction
    predicted_battery_drain = model.predict(input_data)

    # Show the result
    st.write(f"Predicted Battery Drain: {predicted_battery_drain[0]:.2f} mAh")

