import os

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

CUSTOMER_DISTANCE_KM = 100
EARTH_RADIUS_KM = 6371
DUBLIN_OFFICE_LATITUDE = 53.339428
DUBLIN_OFFICE_LONGITUDE = -6.257664
CUSTOMERS_FILE_PATH = os.path.join(dir_path, "data/customers.json")
