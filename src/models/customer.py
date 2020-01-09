from .point import Point


class Customer:
    """Basic customer information."""

    def __init__(self, _id: int, name: str, location: Point):
        self.id = _id
        self.name = name
        self.location = location

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Customer):
            return NotImplemented

        return (
            self.id == other.id
            and self.name == other.name
            and self.location == other.location
        )
