import requests

GOOGLE_MAPS_API_KEY = "api_key"

def get_nearby_hospitals(latitude, longitude):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    params = {
        "key": GOOGLE_MAPS_API_KEY,
        "location": f"{latitude},{longitude}",
        "radius": 5000,
        "type": "hospital"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get("results", [])
