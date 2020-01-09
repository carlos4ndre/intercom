import math


class Point:
    """Point with geographical coordinates."""

    def __init__(self, latitude: float, longitude: float):
        if latitude is None:
            raise ValueError("latitude cannot be empty")

        if longitude is None:
            raise ValueError("longitude cannot be empty")

        if not isinstance(latitude, float):
            raise ValueError("latitude must be float")

        if not isinstance(longitude, float):
            raise ValueError("longitude must be float")

        self.latitude = latitude
        self.longitude = longitude

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return NotImplemented

        return math.isclose(
            self.latitude, self.latitude, rel_tol=1e-5
        ) and math.isclose(self.longitude, self.longitude, rel_tol=1e-5)
