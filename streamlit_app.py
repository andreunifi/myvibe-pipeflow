import streamlit as st
import pandas as pd
import json

# Function to simulate fetching JSON data (replace with actual API call)
def fetch_data():
    # Simulated JSON data
    json_data = [
        {
            "title": "Event 134",
            "description": "Description for Event 1",
            "start_date": "2024-07-01",
            "end_date": "2024-07-03",
            "capienza": 100,
            "price": 10.0,
            "location": "Location A"
        },
        {
            "title": "Event 2",
            "description": "Description for Event 2",
            "start_date": "2024-07-05",
            "end_date": "2024-07-07",
            "capienza": 150,
            "price": 15.0,
            "location": "Location B"
        }
    ]
    return json_data

def main():
    st.title('Event Data Table')
    
    # Button to fetch data
    if st.button('Fetch Data'):
        data = fetch_data()  # Call function to fetch JSON data
        df = pd.DataFrame(data)  # Convert JSON data to pandas DataFrame
        
        # Display the data table
        st.write(df)

if __name__ == '__main__':
    main()
