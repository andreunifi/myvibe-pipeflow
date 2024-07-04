import requests

def get_coordinates(location):
    url = 'https://nominatim.openstreetmap.org/search'
    params = {
        'q': location,
        'format': 'json',
        'addressdetails': 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data:
        lat = data[0].get('lat')
        lon = data[0].get('lon')
        return [float(lat), float(lon)]
    else:
        return None

locations = ["London", "Milan", "France", "Brazil", "South Africa"]
coordinates = {}

for location in locations:
    coord = get_coordinates(location)
    if coord:
        coordinates[location] = coord
    else:
        coordinates[location] = "Coordinates not found"

print(coordinates)
