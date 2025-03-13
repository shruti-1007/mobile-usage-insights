#  Unveiling Mobile Usage Patterns & Battery Drain Prediction  

##  Project Overview  
This project analyzes smartphone usage patterns and predicts battery drain based on factors like screen time, app usage, data consumption, and the number of installed apps. The goal is to provide insights into user behavior and optimize power consumption.  

## Dataset  
***Dataset Source***: [Mobile Device Usage and User Behavior Dataset - Kaggle](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset) <br>
***Dataset features***:  

- **Screen On Time (hours/day)**  
- **App Usage Time (min/day)**  
- **Data Usage (MB/day)**  
- **Number of Apps Installed**  
- **Operating System (Android/iOS)**  
- **Battery Drain (mAh/day) [Target Variable]**  

##  Key Analyses & Visualizations  
- **Correlation Heatmap**: Identifies relationships between features.  
- **Box Plots**: Compares battery drain, screen time, and data usage across OS.  
- **Residual Plot**: Evaluates model performance.  
- **Bar Charts**: Highlights differences in smartphone usage between Android and iOS users.  

## Model & Performance  
- **Algorithm**: Linear Regression  
- **Metrics**:  
  -  **R² Score**: `0.9434`  
  -  **RMSE**: `0.0697`  
- **Residual Analysis**: Ensures model assumptions hold.  

##  Streamlit App Features  
-  **Interactive Visualizations**  
-  **User Input for Predictions**  
-  **Model Performance**  

##  How to Run  
1. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
 ## Contributors
  
- [Shristi Pokhrel](https://github.com/Shri-29)
- [Shruti Maharjan](https://github.com/shruti-1007)

