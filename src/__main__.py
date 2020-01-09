from src.customers import find_customers_by_distance
from src.constants import (
    DUBLIN_OFFICE_LATITUDE,
    DUBLIN_OFFICE_LONGITUDE,
    CUSTOMER_DISTANCE_KM,
)
from tabulate import tabulate


def display_nearby_customers():
    customers = find_customers_by_distance(
        DUBLIN_OFFICE_LATITUDE, DUBLIN_OFFICE_LONGITUDE, CUSTOMER_DISTANCE_KM
    )
    rows = [[customer["user_id"], customer["name"]] for customer in customers]
    print(tabulate(rows, headers=["User ID", "Name"]))


display_nearby_customers()
