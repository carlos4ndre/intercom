import ijson
import logging
from src.constants import (
    DUBLIN_OFFICE_LATITUDE,
    DUBLIN_OFFICE_LONGITUDE,
    CUSTOMERS_FILE_PATH,
)
from src.geo import distance_between_coordinates

logger = logging.getLogger(__name__)


def find_customers_by_distance(latitude, longitude, distance_km):
    results = {}

    with open(CUSTOMERS_FILE_PATH) as ro_file:
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
    distance_km = distance_between_coordinates(
        latitude, longitude, DUBLIN_OFFICE_LATITUDE, DUBLIN_OFFICE_LONGITUDE
    )
    return distance_km < max_distance_km
