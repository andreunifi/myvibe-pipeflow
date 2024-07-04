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

# Title of the app
st.title("Pipeflow")


# Text field
event_query = st.text_input("Enter event query")


list=  '''
[
    {
        "name": "Milan Fashion Week",
        "location": "Milan, Italy",
        "datetime": "September 15th to 21st, 2024",
        "description": "Transforms Milan into the epicenter of the fashion world, with designers showcasing their latest creations.",
        "price": 200.00,
        "capacity": 1000
    },
    {
        "name": "Leonardo da Vinci Exhibition",
        "location": "Museo Nazionale della Scienza e della Tecnologia Leonardo da Vinci, Milan, Italy",
        "datetime": "July 1st to October 31st, 2024",
        "description": "A deep dive into the genius of Leonardo, with intricate sketches, engineering marvels, and timeless artworks.",
        "price": 15.00,
        "capacity": 500
    },
    {
        "name": "Milan Design Week",
        "location": "Various locations in Milan, Italy",
        "datetime": "April 10th to 16th, 2024",
        "description": "A celebration of creativity, with cutting-edge designs, thought-provoking installations, and engaging workshops.",
        "price": 50.00,
        "capacity": 3000
    },
    {
        "name": "La Scala Opera Season Opening",
        "location": "Teatro alla Scala, Milan, Italy",
        "datetime": "December 7th, 2024",
        "description": "A cultural highlight, with world-class performances, a glittering audience, and an atmosphere steeped in tradition.",
        "price": 150.00,
        "capacity": 2000
    },
    {
        "name": "Milan Food Festival",
        "location": "Milan, Italy",
        "datetime": "June 5th to 8th, 2024",
        "description": "A four-day feast, with local delicacies, live cooking demonstrations, and interactive workshops.",
        "price": 25.00,
        "capacity": 10000
    },
    {
        "name": "Oktoberfest",
        "location": "Munich, Germany",
        "datetime": "September 21st to October 6th, 2024",
        "description": "A world-famous beer festival with traditional Bavarian music, food, and culture.",
        "price": 10.00,
        "capacity": 500000
    },
    {
        "name": "Glastonbury Festival",
        "location": "Somerset, England",
        "datetime": "June 26th to 30th, 2024",
        "description": "A five-day festival of contemporary performing arts, featuring music, dance, comedy, theatre, circus, and more.",
        "price": 250.00,
        "capacity": 135000
    }
]
'''
events = classify_and_describe_events(list)

# Convert event data to DataFrame
df = pd.read_json(events)

# Slider to select the number of events to display
max_items = st.slider("Select the maximum number of events to display", min_value=1, max_value=len(df), value=len(df))

# Display the table with a maximum number of items based on the slider
st.table(df.head(max_items))

# Create a map
def create_map(events):
    m = folium.Map(location=[20, 0], zoom_start=2, tiles="cartodb dark_matter")

    for event in events:
        location_name = event[2]
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