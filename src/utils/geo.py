import math
from src.models import Point
from src.constants import EARTH_RADIUS_KM


def convert_degrees_to_radians(value: float) -> float:
    """
    Converts a value in degrees into radians.

    :param float value: Value in degrees
    :return: Value in radians
    :rtype: float
    """
    return value * math.pi / 180


# Credits to https://stackoverflow.com/questions/365826/calculate-distance-between-2-gps-coordinates
def distance_between_points(p1: Point, p2: Point) -> float:
    """
    Calculate the distance in kilometers between two points.

    :param Point p1: First point to calculate the distance
    :param Point p2: Second point to calculate the distance
    :return: Total distance in kilometers between the two points
    :rtype: float
    """
    dlon = convert_degrees_to_radians(p2.longitude - p1.longitude)
    lat1 = convert_degrees_to_radians(p1.latitude)
    lat2 = convert_degrees_to_radians(p2.latitude)

    a = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(
        dlon
    )
    c = math.acos(a)

    return EARTH_RADIUS_KM * c


def is_point_within_range(center: Point, target: Point, max_distance_km: int) -> bool:
    """
    Converts a value in degrees into radians.

    :param Point center: The central location from where the search is performed
    :param Point target: The point we want to analyse its within the range
    :param int max_distance_km: The distance in kilometers that defines the space the point must belong to
    :return: True if the point is within range, False otherwise
    :rtype: bool
    """
    distance_km = distance_between_points(center, target)
    return distance_km < max_distance_km
