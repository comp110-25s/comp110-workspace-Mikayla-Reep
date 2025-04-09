"""File to define Bear class."""

__author__: str = "730648844"


class Bear:
    """Initation and Methods for every bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor method."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """What happens to the bear every day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """When the bear eats."""
        self.hunger_score += num_fish
        return None
