import requests
import json

# Step 1: Data Collection (text-only)
def fetch_text_data_from_sources():
    # Replace with actual data sources
    data_sources = [
        "https://api.example.com/data1",
        "https://api.example.com/data2"
    ]
    
    text_data = []
    for source in data_sources:
        response = requests.get(source)
        if response.status_code == 200:
            text_data.append(response.text)
    return text_data


