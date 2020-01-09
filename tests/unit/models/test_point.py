import pytest
from src.models import Point
from hypothesis import given
from tests.strategies import valid_coordinate, invalid_coordinate_type, empty_coordinate


@given(latitude=valid_coordinate, longitude=valid_coordinate)
def test_initialization(latitude, longitude):
    point = Point(latitude, longitude)

    assert point.latitude == latitude
    assert point.longitude == longitude


@given(latitude=empty_coordinate, longitude=valid_coordinate)
def test_latitude_cannot_be_empty(latitude, longitude):
    error_message = "latitude cannot be empty"

    with pytest.raises(ValueError) as excinfo:
        Point(latitude, longitude)
    assert str(excinfo.value) == error_message


@given(latitude=valid_coordinate, longitude=empty_coordinate)
def test_longitude_cannot_be_empty(latitude, longitude):
    error_message = "longitude cannot be empty"

    with pytest.raises(ValueError) as excinfo:
        Point(latitude, longitude)
    assert str(excinfo.value) == error_message


@given(latitude=invalid_coordinate_type, longitude=valid_coordinate)
def test_latitude_must_be_float(latitude, longitude):
    error_message = "latitude must be float"

    with pytest.raises(ValueError) as excinfo:
        Point(latitude, longitude)
    assert str(excinfo.value) == error_message


@given(latitude=valid_coordinate, longitude=invalid_coordinate_type)
def test_longitude_must_be_float(latitude, longitude):
    error_message = "longitude must be float"

    with pytest.raises(ValueError) as excinfo:
        Point(latitude, longitude)
    assert str(excinfo.value) == error_message


@given(latitude=valid_coordinate, longitude=valid_coordinate)
def test_equality(latitude, longitude):
    assert Point(latitude, longitude) == Point(latitude, longitude)
