import math


class Point:
    def __init__(self, latitude: float, longitude: float):
        if latitude and longitude:
            self.latitude = latitude
            self.longitude = longitude
        else:
            raise ValueError("latitude or longitude cannot be empty")

    def __eq__(self, other):
        return math.isclose(
            self.latitude, self.latitude, rel_tol=1e-5
        ) and math.isclose(self.longitude, self.longitude, rel_tol=1e-5)
