#  Unveiling Mobile Usage Patterns & Battery Drain Prediction  

##  Project Overview  
This project analyzes smartphone usage patterns and predicts battery drain based on factors like screen time, app usage, data consumption, and the number of installed apps. The goal is to provide insights into user behavior and optimize power consumption.  

## Dataset  
***Dataset Source***: [Mobile Device Usage and User Behavior Dataset - Kaggle](https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset) <br> <br>
***Dataset features***:  
- **Device Model**: Model of the user's smartphone.  
- **Operating System**: The OS of the device (iOS or Android).  
- **App Usage Time**: Daily time spent on mobile applications, measured in minutes.  
- **Screen On Time**: Average hours per day the screen is active.  
- **Battery Drain**: Daily battery consumption in mAh.  
- **Number of Apps Installed**: Total apps available on the device.  
- **Data Usage**: Daily mobile data consumption in megabytes.  
- **Age**: Age of the user.  
- **Gender**: Gender of the user (Male or Female).  
- **User Behavior Class**: Classification of user behavior based on usage patterns (1 to 5)  
- ***Gender***: male or female


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
- **Other Algorithms Tested**: RandomForestRegressor
   - **R²** : `0.95`
   - **RMSE**: ` 0.0668 ± 0.0054`

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

