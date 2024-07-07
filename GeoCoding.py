import requests

def get_coordinates(location):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': location,
        'format': 'json',
        'addressdetails': 1
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        
        if data:
            lat = data[0].get('lat')
            lon = data[0].get('lon')
            return [float(lat), float(lon)]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except ValueError as e:
        print(f"JSON decode error: {e}")
        return None