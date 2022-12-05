import requests

class Util:

    def __init__(self):
        self.API_KEY = "AIzaSyA9oQozIsxvLw1qj7p1JXRYC9SvKHSF6ZI"
        self.LOCATION = "45.9636%2C-66.6431"
        self.RADIUS = "10000"

    def getPredictions(self, place):
        params = {
            "input": place,
            "key": self.API_KEY,
            "radius": self.RADIUS
        }
        resp = requests.get("https://maps.googleapis.com/maps/api/place/autocomplete/json?location=45.9636%2C-66.6431&strictbounds=true", params=params)
        resp = resp.json()
        predictions = []
        for prediction in resp['predictions']:
            predictions.append(prediction['description'])
        return predictions

    def durationBetweenTwoLocations(self, origin, destination):
        params = {
            "origins": origin,
            "destinations": destination,
            "key": self.API_KEY
        }
        resp = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json", params=params)
        resp = resp.json()
        return int(resp['rows'][0]['elements'][0]['duration']['value'])