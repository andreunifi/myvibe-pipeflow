import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import GeoCoding
from myVibeGroq import classify_and_describe_events
# Set the page config
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

st.title("Pipeflow")

# Text field for event query

# Text field for URL
url_input = st.text_input("Enter URL to fetch event data")

# Fetch data from URL
if url_input:
    try:
        response = requests.get(url_input)
        response.raise_for_status()
        list = response.text
        events = classify_and_describe_events(list)
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        events = []
else:
    events = []

# Convert event data to DataFrame
if events:
    df = pd.DataFrame(events)

    # Slider to select the number of events to display
    max_items = st.slider("Select the maximum number of events to display", min_value=1, max_value=len(df), value=len(df))

    # Display the table with a maximum number of items based on the slider
    st.table(df.head(max_items))

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