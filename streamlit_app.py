import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import json
import time
from GeoCoding import get_coordinates
from myVibeGroq import classify_and_describe_events

# Streamlit app configuration
st.set_page_config(page_title="Pipeflow", page_icon=":tada:", layout="wide")

# Custom CSS for dark blue background and white text
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .css-1aumxhk {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .css-1lcbmhc {
        color: #ffffff;
    }
    .css-15zrgzn {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .css-18ni7ap {
        color: #ffffff;
    }
    .css-1v3fvcr {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .css-1l02zno {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the app
st.title("Pipeflow")

# Radio button for selecting input method
input_method = st.radio(
    "Select Input Method",
    options=["Parse Long Text", "Pull Data from Instagram"]
)

# Define available Instagram accounts
instagram_accounts = {
    "Account 1": "https://instagram.com/account1",
    "Account 2": "https://instagram.com/account2",
    "Account 3": "https://instagram.com/account3"
}

if input_method == "Parse Long Text":
    # Text area for JSON input
    events = st.text_area("Enter JSON event data")

    # Button to process JSON input
    if st.button("Classify and Describe Events"):
        try:
            events = classify_and_describe_events(events)
        except json.JSONDecodeError as e:
            st.error(f"Error parsing JSON: {e}")
            events = []
        else:
            events = []
else:  # input_method == "Pull Data from Instagram"
    # Dropdown menu to select Instagram account
    selected_account = st.selectbox("Select an Instagram Account", options=list(instagram_accounts.keys()))

    # Fetch and display data for the selected Instagram account
    st.write(f"Fetching data from Instagram account: {selected_account}...")

    with st.spinner("Loading Instagram data..."):
        # Simulate Instagram data fetching with a delay
        time.sleep(2)  # Replace with actual data fetching logic
        
        # Placeholder for Instagram data (Replace with actual data fetching)
        events = json.dumps([
            {"name": "Event 1", "description": "Description 1", "location": "Location 1", "datetime": "2024-07-07T12:00:00Z", "instagram": instagram_accounts[selected_account]},
            {"name": "Event 2", "description": "Description 2", "location": "Location 2", "datetime": "2024-07-08T12:00:00Z", "instagram": instagram_accounts[selected_account]}
        ])

# Convert event data to DataFrame
if events:
    df = pd.read_json(events)

    # Slider to select the number of events to display
    max_items = st.slider("Select the maximum number of events to display", min_value=1, max_value=len(df), value=len(df))

    # Display the table with a maximum number of items based on the slider
    st.table(df.head(max_items))

    # Dropdown menu for selecting events
    event_names = df["name"].tolist()
    selected_name = st.selectbox("Select an Event", options=event_names)
    
    # Display Instagram link for the selected event
    selected_event = df[df["name"] == selected_name].iloc[0]
    st.markdown(f"**Instagram Link:** [View Profile]({selected_event['instagram']})")

    # Create a map
    def create_map(events):
        m = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodb dark_matter")

        for _, event in df.iterrows():
            location_name = event["location"]
            coordinates = get_coordinates(location_name)
            if coordinates:
                folium.Marker(
                    location=coordinates,
                    popup=f"<b>{event['name']}</b><br>{event['description']}<br>{event['datetime']}",
                    icon=folium.Icon(color="lightblue", icon="info-sign")
                ).add_to(m)
            else:
                print(f"Coordinates not found for {location_name}")

        return m

    # Center the map
    st.write("## Map of Locations")
    map_container = st.container()
    with map_container:
        folium_map = create_map(events)
        st_folium(folium_map, width=700)
else:
    st.write("No events to display.")
