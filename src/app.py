import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json


# Function to scale input data manually
def min_max_scale(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

# Function to reverse scaling (inverse scaling)
def inverse_min_max_scale(scaled_value, min_val, max_val):
    return (scaled_value * (max_val - min_val)) + min_val

# Load min-max values
with open('../data/min_max_values.json', 'r') as f:
    min_max_values = json.load(f)


# Load the trained model
model = joblib.load('../models/battery_drain_model.pkl')


# Title of the app
st.title('Battery Drain Analysis')


# Sidebar for navigation
option = st.sidebar.radio("Select an option", ["Battery Drain Prediction", "Data Visualization and Insights"])

if option == "Battery Drain Prediction":
    st.header('Battery Drain Prediction')
    st.image('../src/assets/image.png')
    
    # Input fields for user data
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
        os_type
    ]

    if st.button('Predict Battery Drain'):
        # Prepare input data
        input_data = pd.DataFrame([input_data_scaled], columns=['Screen On Time (hours/day)', 'App Usage Time (min/day)', 'Data Usage (MB/day)', 'Number of Apps Installed', 'Operating System'])
        
        # Make prediction
        predicted_battery_drain = model.predict(input_data)
        predicted_battery_drain = inverse_min_max_scale(predicted_battery_drain[0], min_max_values['Battery Drain (mAh/day)']['min'], min_max_values['Battery Drain (mAh/day)']['max'])
        
        st.write(f"Predicted Battery Drain: {predicted_battery_drain:.2f} mAh")
    
    # Display Model Performance

    if st.button("Show Model Performance"):
        #pre computed values
        r2 = 0.9434
        rmse = 0.0697
        st.subheader("Model Performance")
        st.write(f"**R² Score:** {r2:.4f}")
        st.write( """
                - The model explains 94.34% of the variance in the data, meaning it fits the data very well.
                - A value close to 1 indicates strong predictive power.""")
        st.write(f"**Root Mean Squared Error (RMSE):** {rmse:.4f}")
        st.write("""
                - Measures the average error magnitude. A lower RMSE indicates better accuracy.
                - Since RMSE is quite low, the model's predictions are very close to actual values.""")
        st.image('../visualizations/residual_plot.png')
        st.write("#### Key Insights ")
        st.write("""
                - **Randomly scattered residuals**: Suggests that the model captures the patterns in data well and that linear regression is an appropriate choice.
                - **Red trend line (LOWESS curve) is mostly flat**: Indicates no strong non-linearity in the model.
                - **No clear funnel shape**: Suggests constant variance (homoscedasticity), meaning the model's errors are evenly distributed.
                """)


elif option == "Data Visualization and Insights":
    st.header(' Battery Drain Data Visualization')
    st.subheader("Correlation Heatmap of the Features")
    st.image('../visualizations/correlation_heatmap.png')
    st.write("#### Key Insights ")
    st.markdown("""
- **Everything is connected** – more screen time leads to higher app usage, battery drain, and data consumption.  
- **Screen Time & App Usage (0.95):** More phone use = more active app engagement.  
- **Battery Drain & Installed Apps (0.96):** More apps = higher battery consumption.  
- **Data Usage (0.93-0.94):** Heavy users also consume more data.  
""")

    st.subheader(" Android Vs iOS behaviour Analysis")
    st.write("#### Bar graph")
    st.image('../visualizations/os_type_bar.png')
    st.write("##### Key Insights ")
    st.markdown("""
    - **Battery Drain**: iOS users experience slightly higher battery drain compared to Android users.
    - **Screen On Time**: iOS users also have a slightly higher screen-on time, indicating more active usage.
    - **Data Usage**: iOS users consume more data on average than Android users.""")
    st.write("#### Box plot")
    st.image('../visualizations/os_boxplot.png')
    st.write("##### Key Insights ")
    st.markdown("""
- **Battery Drain**: Android and iOS users experience similar battery consumption, with a wide variation in both. No significant difference is observed.
- **Screen On Time**: Both platforms have comparable screen-on times, suggesting similar usage patterns.
- **Data Usage**: Android and iOS users consume data at nearly the same rate, with no clear outliers.
             """)
    
    st.subheader("Screen-On Time Analysis")
    st.write("#### Distribution plot for different user categories")
    st.image('../visualizations/screen_on_time_class.png')
    st.write("##### Key Insights ")
    st.markdown("""
**📈 Positive Correlation**  
- As the **Behavior Class** increases (1 → 5), **Screen-on Time** also increases consistently.  
- This suggests that users in higher behavior classes spend **more time** on their screens daily.  

**📊 Spread & Variability**  
- **Lower classes (1 & 2):** Smaller interquartile ranges (IQR), meaning screen-on time is **more consistent** among users.  
- **Higher classes (4 & 5):** Larger IQR, meaning screen-on time **varies significantly** among users.  

**🔍 Outliers & Extreme Values**  
- Some **extreme values** appear in all behavior classes.  
- **Higher classes (4 & 5):** Wider range, suggesting some users in these classes **use their screens significantly more** than the median.  
""")

    st.write('#### Screen on time according to Gender')
    st.image("../visualizations/screen_on_time_gender.png")
    st.write("##### Key Insights ")
    st.markdown(""" 
- Median screen-on time is similar for both genders.
- Variability (IQR) is nearly identical, meaning consistent usage patterns.
- Outliers exist in both groups, indicating some heavy users.
- No significant gender-based difference in screen usage.
                """)

