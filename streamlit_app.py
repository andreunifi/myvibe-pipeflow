import streamlit as st
import pandas as pd
import numpy as np

# Sample Data
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)

# Toggle theme
theme = st.sidebar.selectbox('Select Theme', ['Light', 'Dark'])

# Apply CSS for themes and card styling
if theme == 'Dark':
    st.markdown("""
        <style>
            body {
                background-color: #0E1117;
                color: #FFFFFF;
            }
            .sidebar .sidebar-content {
                background-color: #262730;
                color: #FFFFFF;
            }
            .st-cm {
                color: #FFFFFF;
            }
            .card {
                background-color: #1E1E1E;
                color: #FFFFFF;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                margin-bottom: 20px;
            }
            .dataframe {
                border-collapse: collapse;
                width: 100%;
                margin-top: 20px;
            }
            .dataframe th, .dataframe td {
                text-align: left;
                padding: 8px;
                border-bottom: 1px solid #ddd;
            }
            .dataframe tr:nth-child(even) {
                background-color: #2E2E2E;
            }
            .dataframe th {
                background-color: #555555;
                color: white;
            }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            body {
                background-color: #FFFFFF;
                color: #000000;
            }
            .sidebar .sidebar-content {
                background-color: #F4F4F4;
                color: #000000;
            }
            .st-cm {
                color: #000000;
            }
            .card {
                background-color: #FFFFFF;
                color: #000000;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-bottom: 20px;
            }
            .dataframe {
                border-collapse: collapse;
                width: 100%;
                margin-top: 20px;
            }
            .dataframe th, .dataframe td {
                text-align: left;
                padding: 8px;
                border-bottom: 1px solid #ddd;
            }
            .dataframe tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            .dataframe th {
                background-color: #4CAF50;
                color: white;
            }
        </style>
        """, unsafe_allow_html=True)

# Dashboard Title
st.title('Minimal Dashboard with Stylish Table')

# Display Data inside a Card
st.markdown('<div class="card">', unsafe_allow_html=True)
st.header('Sample Data')
st.write(data)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.sidebar.text('Theme by Streamlit')

# Run the app using: streamlit run <filename.py>
