from src.models import Customer
from hypothesis import given
from tests.strategies import valid_customer_id, valid_customer_name, valid_point


@given(user_id=valid_customer_id, name=valid_customer_name, location=valid_point)
def test_initialization(user_id, name, location):
    customer = Customer(user_id, name, location)

    assert customer.id == user_id
    assert customer.name == name
    assert customer.location == location


@given(user_id=valid_customer_id, name=valid_customer_name, location=valid_point)
def test_equality(user_id, name, location):
    customer1 = Customer(user_id, name, location)
    customer2 = Customer(user_id, name, location)
    assert customer1 == customer2
