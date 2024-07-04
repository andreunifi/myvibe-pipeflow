import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Set the page config
st.set_page_config(page_title="Pipeflow", page_icon=":tada:", layout="wide")

# Custom CSS for dark theme
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
        background-color: #333333;
        color: #ffffff;
    }
    .css-18ni7ap {
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

# Example event data
events = [
    {
        "name": "Milan Fashion Week",
        "location": "Milan",
        "datetime": "September 15th to 21st, 2024",
        "description": "Transforms Milan into the epicenter of the fashion world, with designers showcasing their latest creations.",
        "price": None,
        "capacity": None
    },
    {
        "name": "Leonardo da Vinci Exhibition",
        "location": "Museo Nazionale della Scienza e della Tecnologia Leonardo da Vinci",
        "datetime": "July 1st to October 31st, 2024",
        "description": "A deep dive into the genius of Leonardo, with intricate sketches, engineering marvels, and timeless artworks.",
        "price": None,
        "capacity": None
    },
    {
        "name": "Milan Design Week",
        "location": "Various locations",
        "datetime": "April 10th to 16th, 2024",
        "description": "A celebration of creativity, with cutting-edge designs, thought-provoking installations, and engaging workshops.",
        "price": None,
        "capacity": None
    },
    {
        "name": "La Scala Opera Season Opening",
        "location": "Teatro alla Scala",
        "datetime": "December 7th, 2024",
        "description": "A cultural highlight, with world-class performances, a glittering audience, and an atmosphere steeped in tradition.",
        "price": None,
        "capacity": None
    },
    {
        "name": "Milan Food Festival",
        "location": "Milan",
        "datetime": "June 5th to 8th, 2024",
        "description": "A four-day feast, with local delicacies, live cooking demonstrations, and interactive workshops.",
        "price": None,
        "capacity": None
    }
]

# Convert event data to DataFrame
df = pd.DataFrame(events)

# Slider to select the number of events to display
max_items = st.slider("Select the maximum number of events to display", min_value=1, max_value=len(df), value=len(df))

# Display the table with a maximum number of items based on the slider
st.table(df.head(max_items))

# Create a map
def create_map():
    m = folium.Map(location=[0, 0], zoom_start=2, tiles="cartodb dark_matter")
    
    locations = {
        "United States": [37.0902, -95.7129],
        "Sweden": [60.1282, 18.6435],
        "France": [46.6034, 1.8883],
        "Brazil": [-14.2350, -51.9253],
        "South Africa": [-30.5595, 22.9375]
    }
    
    for loc, coords in locations.items():
        folium.Marker(
            location=coords,
            popup=loc,
            icon=folium.Icon(color="lightblue", icon="info-sign")
        ).add_to(m)
    
    return m

# Display the map
st_folium(create_map(), width=700)

