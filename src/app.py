import streamlit as st
import plotly.express as px
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

# Page configuration
st.set_page_config(page_title="Mobile Data Insights", layout="wide")

# Utility functions
def battery_saving_recommendations(screen_on_time, app_usage_time, data_usage, number_of_apps, os_type):
    recommendations = []

    if screen_on_time > 6:
        recommendations.append("Consider reducing screen-on time to save battery. Try using battery saver modes.")

    if app_usage_time > 180:
        recommendations.append("Reducing app usage can help conserve battery. Try limiting background app activity.")

    if data_usage > 1000:
        recommendations.append("High data usage impacts battery life. Use Wi-Fi more often or reduce heavy app usage.")

    if number_of_apps > 50:
        recommendations.append("Uninstall unnecessary apps to reduce battery drain.")

    if os_type == 1:
        recommendations.append("iOS users can enable Low Power Mode to extend battery life.")
    else:
        recommendations.append("Android users can activate Battery Saver Mode for better battery management.")

    return recommendations

def min_max_scale(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val != min_val else 0

def inverse_min_max_scale(scaled_value, min_val, max_val):
    return (scaled_value * (max_val - min_val)) + min_val

# Load necessary resources
with open('../data/min_max_values.json', 'r') as f:
    min_max_values = json.load(f)

model = joblib.load('../models/battery_drain_model.pkl')

# Sidebar navigation
option = st.sidebar.radio("Select an option", ["Battery Drain Prediction", "Data Visualization and Insights", "Hypothesis Testing Results"])

# Option 1: Data Visualization
if option == "Data Visualization and Insights":
    st.title("📊 Mobile Data Insights")
    st.markdown("### 🔹 Key Averages")

    metrics_col = st.columns(5)
    card_style = """
        background-color: #fffbcc;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin: 10px;
        color: black;
    """

    metrics = [
        ("📱 271.1 min/day", "App Usage Time"),
        ("💡 5.27 hrs/day", "Screen On Time"),
        ("🔋 1525 mAh/day", "Battery Drain"),
        ("📦 51", "Apps Installed"),
        ("📶 929.7 MB/day", "Data Usage")
    ]

    for col, (value, label) in zip(metrics_col, metrics):
        col.markdown(f'<div style="{card_style}"><h3>{value}</h3><p>{label}</p></div>', unsafe_allow_html=True)

    st.markdown("----------")
    st.markdown("### 📌 Exploratory Data Analysis")
    
    metrics_data = [
        ("../visualizations/correlation_heatmap.png", "Correlation Heatmap")
    ]
    for i in range(0, len(metrics_data), 1):
        cols = st.columns(1)
        for j in range(1):
            if i + j < len(metrics_data):
                image_url, title = metrics_data[i + j]
                with cols[j]:
                    st.markdown(f"### {title}")
                    st.image(image_url, use_container_width=True)
                    with st.expander(f"🔍 View Insights: {title}", expanded=False):
                        st.markdown(f"### Insights for {title}")
                        st.write("- Example insights will be listed here.")
                        st.markdown("- Helps understand screen on time trends and battery usage behavior.")
    st.markdown("--------------------")
    st.markdown("### 📌 Android Vs iOS Behavior Analysis")

    metrics_data = [
        ("../visualizations/os_distribution.png", "OS Type Distribution"),
        ("../visualizations/os_type_bar.png", "iOS vs Android Battery Drain"),
        ("../visualizations/os_boxplot.png", "Battery Drain by OS Type")
    ]

    for i in range(0, len(metrics_data), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(metrics_data):
                image_url, title = metrics_data[i + j]
                with cols[j]:
                    st.markdown(f"### {title}")
                    st.image(image_url, use_container_width=True)
                    with st.expander(f"🔍 View Insights: {title}", expanded=False):
                        st.markdown(f"### Insights for {title}")
                        st.write("- Example insights will be listed here.")
                        st.markdown("- Helps understand OS trends and battery usage behavior.")
    st.markdown("--------------------")
    st.markdown("### 📌 Screen On time Analysis")
    
    metrics_data = [
        ("../visualizations/screen_on_time_class.png", "Screen On Time Class Distribution"),
        ("../visualizations/screen_on_time_gender.png", "Screen On Time Gender Distribution"),
        ("../visualizations/screen_on_time_vs_battery_drain.png", "Screen On Time vs Battery Drain")
    ]
    for i in range(0, len(metrics_data), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(metrics_data):
                image_url, title = metrics_data[i + j]
                with cols[j]:
                    st.markdown(f"### {title}")
                    st.image(image_url, use_container_width=True)
                    with st.expander(f"🔍 View Insights: {title}", expanded=False):
                        st.markdown(f"### Insights for {title}")
                        st.write("- Example insights will be listed here.")
                        st.markdown("- Helps understand screen on time trends and battery usage behavior.")
    
    
    st.markdown("--------------------")
    st.markdown("### 📌 Battery Drain Analysis")
    
    metrics_data = [
        ("../visualizations/app_usage_time_vs_battery_drain.png", "App Usage Time vs Battery Drain"),
        ("../visualizations/data_consumption_vs_battery_drain.png", "Data Usage vs Battery Drain"),
        ("../visualizations/number_of_apps_installed_vs_battery_drain.png", "Number of Apps vs Battery Drain"),
        ("../visualizations/screen_on_time_vs_battery_drain.png", "Screen On Time vs Battery Drain")
    ]
    for i in range(0, len(metrics_data), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(metrics_data):
                image_url, title = metrics_data[i + j]
                with cols[j]:
                    st.markdown(f"### {title}")
                    st.image(image_url, use_container_width=True)
                    with st.expander(f"🔍 View Insights: {title}", expanded=False):
                        st.markdown(f"### Insights for {title}")
                        st.write("- Example insights will be listed here.")
                        st.markdown("- Helps understand screen on time trends and battery usage behavior.")
# Option 2: Hypothesis Testing
elif option == "Hypothesis Testing Results":
    st.markdown("### 🔬 Hypothesis Testing Results")

    hypothesis_results = {
        "Data Usage Change": {
            "null_hypothesis": "Is there a **significant change** in mobile data usage before and after the app update?",
            "test_statistic": 2.3,
            "p_value": 0.03,
            "result": "Significant Change",
            "insight": "Data usage increased significantly after the app update."
        },
        "Battery Drain Comparison": {
            "null_hypothesis": "Does **Device A** experience more **battery drain** than **Device B**?",
            "test_statistic": -0.5,
            "p_value": 0.62,
            "result": "No Significant Difference",
            "insight": "No significant battery drain difference between Device A and Device B."
        }
    }

    for test_name, test_data in hypothesis_results.items():
        with st.expander(f"Test: {test_name}", expanded=False):
            st.markdown(f"""
                <div style="font-size: 20px; font-weight: bold; color: #4CAF50; background-color: #e7f7e7; padding: 10px; border-radius: 8px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
                    🤔 <b>{test_data['null_hypothesis']}</b>
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"**Test Statistic**: {test_data['test_statistic']}")
            st.markdown(f"**P-value**: {test_data['p_value']}")

            if test_data['p_value'] < 0.05:
                st.markdown(f"""
                    <div style="background-color: #d4edda; padding: 15px; border-radius: 8px;">
                        <span style="color: green; font-weight: bold;">✅ **Result**: {test_data['result']} 🔥</span>
                        <p>{test_data['insight']}</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="background-color: #f8d7da; padding: 15px; border-radius: 8px;">
                        <span style="color: red; font-weight: bold;">❌ **Result**: {test_data['result']}</span>
                        <p>{test_data['insight']}</p>
                    </div>
                """, unsafe_allow_html=True)

# Option 3: Battery Drain Prediction
elif option == "Battery Drain Prediction":
    st.header("🔋 Battery Drain Prediction")
    st.image('../src/assets/image.png')

    # Input fields
    screen_on_time = st.number_input('Screen On Time (hours/day)', min_value=0.0, max_value=24.0, value=5.0)
    app_usage_time = st.number_input('App Usage Time (minutes/day)', min_value=0, value=120)
    data_usage = st.number_input('Data Usage (MB/day)', min_value=0, value=500)
    number_of_apps = st.number_input('Number of Apps Installed', min_value=0, value=30)
    os_label = st.selectbox('Operating System', ['Android', 'iOS'])
    os_type = 1 if os_label == 'iOS' else 0

    # Prepare scaled input
    input_data_scaled = [
        min_max_scale(screen_on_time, min_max_values['Screen On Time (hours/day)']['min'], min_max_values['Screen On Time (hours/day)']['max']),
        min_max_scale(app_usage_time, min_max_values['App Usage Time (min/day)']['min'], min_max_values['App Usage Time (min/day)']['max']),
        min_max_scale(data_usage, min_max_values['Data Usage (MB/day)']['min'], min_max_values['Data Usage (MB/day)']['max']),
        min_max_scale(number_of_apps, min_max_values['Number of Apps Installed']['min'], min_max_values['Number of Apps Installed']['max']),
        os_type
    ]

    if st.button('Predict Battery Drain'):
        input_df = pd.DataFrame([input_data_scaled], columns=[
            'Screen On Time (hours/day)', 'App Usage Time (min/day)',
            'Data Usage (MB/day)', 'Number of Apps Installed', 'Operating System'
        ])
        predicted_scaled = model.predict(input_df)[0]
        predicted_battery_drain = inverse_min_max_scale(predicted_scaled, min_max_values['Battery Drain (mAh/day)']['min'], min_max_values['Battery Drain (mAh/day)']['max'])
        st.success(f"🔋 Predicted Battery Drain: {predicted_battery_drain:.2f} mAh")

    if st.button('Show Battery Saving Tips'):
        tips = battery_saving_recommendations(screen_on_time, app_usage_time, data_usage, number_of_apps, os_type)
        st.markdown("#### 🔧 Recommended Battery Saving Tips:")
        for tip in tips:
            st.markdown(f"- {tip}")

    if st.button("Show Model Performance"):
        st.subheader("📈 Model Performance")
        r2 = 0.9434
        rmse = 0.0697

        st.write(f"**R² Score:** {r2:.4f} — explains 94.34% variance in data.")
        st.write(f"**RMSE:** {rmse:.4f} — low error means high prediction accuracy.")
        st.image('../visualizations/residual_plot.png')
        st.markdown("#### Key Insights")
        st.write("""
            - **Residuals are randomly scattered**: Model captures patterns well.
            - **Flat LOWESS curve**: Indicates a linear model is appropriate.
            - **No funnel shape**: Suggests consistent variance (homoscedasticity).
        """)
