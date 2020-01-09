import math
import logging
from src.models import Point
from src.constants import EARTH_RADIUS_KM

logger = logging.getLogger(__name__)


def convert_degrees_to_radians(value: float) -> float:
    return value * math.pi / 180


# Credits to https://stackoverflow.com/questions/365826/calculate-distance-between-2-gps-coordinates
def distance_between_points(p1: Point, p2: Point) -> float:
    dlat = convert_degrees_to_radians(p2.latitude - p1.latitude)
    dlon = convert_degrees_to_radians(p2.longitude - p1.longitude)
    lat1 = convert_degrees_to_radians(p1.latitude)
    lat2 = convert_degrees_to_radians(p2.latitude)

    a = math.pow(math.sin(dlat / 2), 2) + math.pow(math.sin(dlon / 2), 2) * math.cos(
        lat1
    ) * math.cos(lat2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return EARTH_RADIUS_KM * c


def is_point_within_range(center: Point, target: Point, max_distance_km: int) -> bool:
    distance_km = distance_between_points(center, target)
    return distance_km < max_distance_km
