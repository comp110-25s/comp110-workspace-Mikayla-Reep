"""File to define Fish class."""


class Fish:
    """Initiation and Methods that affect the fish"""

    age: int

    def __init__(self):
        """Constructor"""
        self.age = 0
        return None

    def one_day(self):
        "What happens to a fish in one day"
        self.age += 1
        return None
