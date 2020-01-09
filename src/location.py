import math
import ijson
import logging

DEFAULT_DISTANCE_KM = 100
DUBLIN_OFFICE_LATITUDE = 53.339428
DUBLIN_OFFICE_LONGITUDE = -6.257664
CUSTOMERS_FILE = "samples/customers.json"

logger = logging.getLogger(__name__)


def find_customers(distance_km=DEFAULT_DISTANCE_KM):
    results = {}

    with open(CUSTOMERS_FILE) as ro_file:
        logger.info("Find customers within {} km".format(distance_km))
        all_customers = ijson.items(ro_file, "customers.item")
        for customer in all_customers:
            customer_id = customer.get("user_id")
            latitude = customer.get("latitude")
            longitude = customer.get("longitude")

            if latitude and longitude:
                latitude = float(latitude)
                longitude = float(longitude)
                if is_customer_within_range(latitude, longitude, distance_km):
                    results[customer_id] = customer
                    logger.debug("Customer id {} is within range", customer_id)
                else:
                    logger.debug("Customer id {} is not within range", customer_id)
            else:
                logger.warn("Customer id {} has empty coordinates", customer_id)
    sorted_results = [v for (k, v) in sorted(results.items())]
    return sorted_results


def is_customer_within_range(latitude, longitude, max_distance_km):
    distance_km = distance_between_gps_coordinates(
        latitude, longitude, DUBLIN_OFFICE_LATITUDE, DUBLIN_OFFICE_LONGITUDE
    )
    return distance_km < max_distance_km


def convert_degrees_to_radians(value):
    return value * math.pi / 180


# Credits to https://stackoverflow.com/questions/365826/calculate-distance-between-2-gps-coordinates
def distance_between_gps_coordinates(lat1, lon1, lat2, lon2):
    earth_radius_km = 6371

    dlat = convert_degrees_to_radians(lat2 - lat1)
    dlon = convert_degrees_to_radians(lon2 - lon1)
    lat1 = convert_degrees_to_radians(lat1)
    lat2 = convert_degrees_to_radians(lat2)

    a = math.pow(math.sin(dlat / 2), 2) + math.pow(math.sin(dlon / 2), 2) * math.cos(
        lat1
    ) * math.cos(lat2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return earth_radius_km * c
