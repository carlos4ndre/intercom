import pytest
from src.customers import find_customers_by_distance

LATITUDE = 53.339428
LONGITUDE = -6.257664
USER_ID_4 = {"latitude": "53.2451022", "longitude": "-6.238335", "name": "Ian Kehoe", "user_id": 4}
USER_ID_5 = {"latitude": "53.1302756", "longitude": "-6.2397222", "name": "Nora Dempsey", "user_id": 5}
USER_ID_6 = {"latitude": "53.1229599", "longitude": "-6.2705202", "name": "Theresa Enright", "user_id": 6}
USER_ID_11 = {"latitude": "53.008769", "longitude": "-6.1056711", "name": "Richard Finnegan", "user_id": 11}
USER_ID_36 = {"latitude": "53.0033946", "longitude": "-6.3877505", "name": "Lisa Ahearn", "user_id": 39}


@pytest.mark.parametrize("distance_km, expected", [
    # (distance, [sorted user_ids])
    (1, []),
    (10, []),
    (20, [USER_ID_4]),
    (30, [USER_ID_4, USER_ID_5, USER_ID_6]),
    (40, [USER_ID_4, USER_ID_5, USER_ID_6, USER_ID_11, USER_ID_36]),
])
def test_find_customers_by_distance(distance_km, expected):
    assert find_customers_by_distance(LATITUDE, LONGITUDE, distance_km) == expected
