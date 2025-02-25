import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
df = pd.read_csv('C:/Users/Acer/Desktop/Data Science Project/data/preprocessed_data.csv')

# Title of the dashboard
st.title('Battery Drain Analysis Dashboard')

# Show the dataset
st.subheader('Battery Drain Data')
st.write(df)



# Visualizations
# 1. Scatter plot: Battery drain vs Screen-on time
st.subheader('Scatter Plot: Battery Drain vs Screen-On Time')
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='Screen On Time (hours/day)', y='Battery Drain (mAh/day)', ax=ax)
st.pyplot(fig)

# 2. Scatter plot: Battery drain vs Data Usage 
st.subheader('Scatter Plot: Battery Drain vs Data Usage')
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='Data Usage (MB/day)', y='Battery Drain (mAh/day)', ax=ax)
st.pyplot(fig)

# 3. Scatter plot: Battery drain vs App Usage Time
st.subheader('Scatter Plot: Battery Drain vs App Usage Time')
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='App Usage Time (min/day)', y='Battery Drain (mAh/day)', ax=ax)
st.pyplot(fig)

# 3. Scatter plot: Battery drain vs Number of Apps Installed
st.subheader('Scatter Plot: Battery Drain vs Number of Apps Installed')
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='Number of Apps Installed', y='Battery Drain (mAh/day)', ax=ax)
st.pyplot(fig)

