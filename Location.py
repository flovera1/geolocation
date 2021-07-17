from pprint import pprint


class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def print_location(self):
        pprint(f"{self.latitude} {self.longitude}")

