import streamlit as st
import plotly.express as px

# Sidebar for navigation
    # Set page config
st.set_page_config(page_title="Mobile Data Insights", layout="wide")
option = st.sidebar.radio("Select an option", ["Battery Drain Prediction", "Data Visualization and Insights", "Hypothesis TestingnResults"])
if option == "Data Visualization and Insights":


    # Title
    st.title("📊 Mobile Data Insights")

    # Average Metrics Display with equal layout
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

    with metrics_col[0]:
        st.markdown(f'<div style="{card_style}"><h3 style="color:black;">📱 271.1 min/day</h3><p style="color:black;">App Usage Time</p></div>', unsafe_allow_html=True)
    with metrics_col[1]:
        st.markdown(f'<div style="{card_style}"><h3 style="color:black;">💡 5.27 hrs/day</h3><p style="color:black;">Screen On Time</p></div>', unsafe_allow_html=True)
    with metrics_col[2]:
        st.markdown(f'<div style="{card_style}"><h3 style="color:black;">🔋 1525 mAh/day</h3><p style="color:black;">Battery Drain</p></div>', unsafe_allow_html=True)
    with metrics_col[3]:
        st.markdown(f'<div style="{card_style}"><h3 style="color:black;">📦 51</h3><p style="color:black;">Apps Installed</p></div>', unsafe_allow_html=True)
    with metrics_col[4]:
        st.markdown(f'<div style="{card_style}"><h3 style="color:black;">📶 929.7 MB/day</h3><p style="color:black;">Data Usage</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # 📌 User Metrics Overview (Two Images Per Row)
    st.markdown("### 📌 Android Vs iOS Behavior Analysis")

    # Define chart images
    metrics_data = [
        ("../visualizations/os_distribution.png", "OS Type Distribution"),
        ("../visualizations/os_type_bar.png", "iOS vs Android Battery Drain"),
        ('../visualizations/os_boxplot.png', "Battery Drain by OS Type"),
        # Add more metrics data here
    ]

    # Box styling
    box_style = """
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 4px 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    """

    # Display charts in two columns (two images per row)
    for i in range(0, len(metrics_data), 2):
        cols = st.columns(2)  # Create two columns
        
        for j in range(2):
            if i + j < len(metrics_data):
                image_url, title = metrics_data[i + j]
                with cols[j]:  # Place each image inside the respective column
                    st.markdown(f"### {title}")
                    
                    # Show large image (chart)
                    st.image(image_url, width=500, use_container_width=True)

                    # Styled button for insights
                    with st.expander(f"🔍 View Insights: {title}", expanded=False):
                        # Better user-friendly insights presentation
                        st.markdown(f"### Insights for {title}")
                        st.write(f"📄 Detailed insights for {title} will go here... You can add more detailed analysis, graphs, or descriptions about the data visualization.")
                        
                        # Example: Add some data or explanation
                        st.markdown("- For example, the OS Type Distribution chart shows the percentage of users using each mobile OS.")
                        st.markdown("- The majority of users in this dataset are using Android devices.")
                        st.markdown("- This chart helps us understand the market share of different operating systems, which can be used for targeting mobile app development.")

                    st.markdown("</div>", unsafe_allow_html=True)
elif option == "Hypothesis TestingnResults":
# import scipy.stats as stats
    import matplotlib.pyplot as plt

    # Example of hypotheses and results
    hypothesis_results = {
        "Data Usage Change": {
            "null_hypothesis": "Is there a **significant change** in mobile data usage before and after the app update?",
            "test_statistic": 2.3,
            "p_value": 0.03,
            "result": "Significant Change",
            "insight": "The data usage increased significantly after the app update."
        },
        "Battery Drain Comparison": {
            "null_hypothesis": "Does **Device A** experience more **battery drain** than **Device B**?",
            "test_statistic": -0.5,
            "p_value": 0.62,
            "result": "No Significant Difference",
            "insight": "There was no significant difference in battery drain between Device A and Device B."
        }
    }

    # Display hypothesis test results with engaging questions
    st.markdown("### 🔬 Hypothesis Testing Results")

    for test_name, test_data in hypothesis_results.items():
        with st.expander(f"Test: {test_name}", expanded=False):
            # Stylish header for the null hypothesis question
            st.markdown(f"""
                <div style="font-size: 20px; font-weight: bold; color: #4CAF50; background-color: #e7f7e7; padding: 10px; border-radius: 8px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
                    🤔 <b>{test_data['null_hypothesis']}</b>
                </div>
            """, unsafe_allow_html=True)
            
            # Display test statistic and p-value with a color-coded approach
            st.markdown(f"**Test Statistic**: {test_data['test_statistic']}")
            st.markdown(f"**P-value**: {test_data['p_value']}")

            # Visualizing the result
            if test_data['p_value'] < 0.05:
                st.markdown(f"""
                    <div style="background-color: #d4edda; padding: 15px; border-radius: 8px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
                        <span style="color: green; font-weight: bold;">✅ **Result**: {test_data['result']} 🔥</span>
                        <p>{test_data['insight']}</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="background-color: #f8d7da; padding: 15px; border-radius: 8px; box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
                        <span style="color: red; font-weight: bold;">❌ **Result**: {test_data['result']} </span>
                        <p>{test_data['insight']}</p>
                    </div>
                """, unsafe_allow_html=True)


