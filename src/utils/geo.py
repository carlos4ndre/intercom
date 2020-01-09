import math
import logging
from src.constants import EARTH_RADIUS_KM

logger = logging.getLogger(__name__)


def convert_degrees_to_radians(value: float) -> float:
    return value * math.pi / 180


# Credits to https://stackoverflow.com/questions/365826/calculate-distance-between-2-gps-coordinates
def distance_between_coordinates(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> float:
    dlat = convert_degrees_to_radians(lat2 - lat1)
    dlon = convert_degrees_to_radians(lon2 - lon1)
    lat1 = convert_degrees_to_radians(lat1)
    lat2 = convert_degrees_to_radians(lat2)

    a = math.pow(math.sin(dlat / 2), 2) + math.pow(math.sin(dlon / 2), 2) * math.cos(
        lat1
    ) * math.cos(lat2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return EARTH_RADIUS_KM * c
