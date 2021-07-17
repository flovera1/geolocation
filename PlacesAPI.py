import requests
from urllib.parse import urlencode


api_key = "AIzaSyAtkUswEgSgGbODpMZtOoWm4N5-z3_t3N8"
lat, lng = 0.0, 0.0
base_endpoint_places = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"


def get_location(sentence):
    params = {
        "key": api_key,
        "input": f"{sentence}",
        "inputtype": "textquery",
        "fields": "place_id,formatted_address,name,geometry,permanently_closed"
    }
    location_bias = f"point:{lat},{lng}"
    circular = True
    return request_api(location_bias, params, circular)


def request_api(locationbias, params, use_cirular):
    locationbias = use_circular(locationbias, use_cirular)
    params['locationbias'] = locationbias
    params_encoded = urlencode(params)
    places_endpoint = f"{base_endpoint_places}?{params_encoded}"
    response = requests.get(places_endpoint)
    resp_json_payload = response.json()
    if len(resp_json_payload['candidates']) == 0:
        return []
    else:
        return resp_json_payload['candidates'][0]['geometry']['location']


def use_circular(locationbias, use_cirular):
    if use_cirular:
        radius = 5000
        locationbias = f"circle:{radius}@{lat},{lng}"
    return locationbias

