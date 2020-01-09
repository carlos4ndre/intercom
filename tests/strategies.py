from src.models import Customer, Point
from hypothesis.strategies import builds, floats, integers, text, none, one_of


# Coordinate
valid_coordinate = floats(allow_nan=False, allow_infinity=False)
empty_coordinate = none()
invalid_coordinate_type = one_of(text(), integers())

# Point
valid_point = builds(Point, valid_coordinate, valid_coordinate)

# Customer
valid_customer_id = integers()
valid_customer_name = text()
valid_customer = builds(Customer, valid_customer_id, valid_customer_name, valid_point)
