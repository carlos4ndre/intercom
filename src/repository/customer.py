import ijson
import logging
from src.constants import CUSTOMERS_FILE_PATH
from src.utils.geo import is_point_within_range
from src.models import Point, Customer
from typing import List

logger = logging.getLogger(__name__)


class CustomerStore:
    @staticmethod
    def find_customers_by_distance(center: Point, distance_km: int) -> List[Customer]:
        results = {}

        with open(CUSTOMERS_FILE_PATH) as ro_file:
            logger.info("Find customers within {} km".format(distance_km))
            all_customers = [
                Customer(
                    c["user_id"],
                    c["name"],
                    Point(float(c["latitude"]), float(c["longitude"])),
                )
                for c in ijson.items(ro_file, "customers.item")
            ]
            for customer in all_customers:
                if is_point_within_range(center, customer.location, distance_km):
                    results[customer.id] = customer
                    logger.debug("Customer id {} is within range", customer.id)
                else:
                    logger.debug("Customer id {} is not within range", customer.id)
        sorted_results = [v for (k, v) in sorted(results.items())]
        return sorted_results
