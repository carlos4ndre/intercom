import pytest
from src.repository import CustomerStore
from src.models import Point, Customer

POINT = Point(53.339428, -6.257664)
USER_ID_4 = Customer(4, "Ian Kehoe", Point(53.2451022, -6.238335))
USER_ID_5 = Customer(5, "Nora Dempsey", Point(53.1302756, -6.2397222))
USER_ID_6 = Customer(6, "Theresa Enright", Point(53.1229599, -6.2705202))
USER_ID_11 = Customer(11, "Richard Finnegan", Point(53.008769, -6.1056711))
USER_ID_36 = Customer(39, "Lisa Ahearn", Point(53.0033946, -6.3877505))


@pytest.mark.parametrize(
    "distance_km, expected",
    [
        # (distance, [sorted user_ids])
        (1, []),
        (10, []),
        (20, [USER_ID_4]),
        (30, [USER_ID_4, USER_ID_5, USER_ID_6]),
        (40, [USER_ID_4, USER_ID_5, USER_ID_6, USER_ID_11, USER_ID_36]),
    ],
)
def test_find_customers_by_distance(distance_km, expected):
    assert CustomerStore.find_customers_by_distance(POINT, distance_km) == expected
