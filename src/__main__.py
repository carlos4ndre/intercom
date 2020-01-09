from src.repository import CustomerStore
from src.models import Point
from src.constants import (
    DUBLIN_OFFICE_LATITUDE,
    DUBLIN_OFFICE_LONGITUDE,
    CUSTOMER_DISTANCE_KM,
)
from tabulate import tabulate


def display_nearby_customers():
    """Show to the user all the customers near the intercom office for the given distance in kilometers."""
    intercom_office_location = Point(DUBLIN_OFFICE_LATITUDE, DUBLIN_OFFICE_LONGITUDE)
    customers = CustomerStore.find_customers_by_distance(
        intercom_office_location, CUSTOMER_DISTANCE_KM
    )
    rows = [[customer.id, customer.name] for customer in customers]
    print(tabulate(rows, headers=["User ID", "Name"]))


def main():
    display_nearby_customers()


main()
