"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear

__author__: str = "730648844"


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears, and removes old one from the list"""

        # lists to keep tract of old animals
        old_fish: list[Fish] = []
        old_bears: list[Bear] = []

        # Finds fish older than 3
        for f in self.fish:
            if f.age > 3:
                old_fish.append(f)

        # Finds bears older than 5
        for b in self.bears:
            if b.age > 5:
                old_bears.append(b)

        # Removes the old fish
        for f in self.fish:
            if f in old_fish:
                self.fish.remove(f)

        # Removes the old bears
        for b in self.bears:
            if b in old_bears:
                self.bears.remove(b)

        return None

    def bears_eating(self):
        for b in self.bears:
            if len(self.fish) >= 5:
                b.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):

        hungry_bears: list[Bear] = []

        for b in self.bears:
            if b.hunger_score < 0:
                hungry_bears.append(b)

        for b in self.bears:
            if b in hungry_bears:
                self.bears.remove(b)
        return None

    def repopulate_fish(self):
        initial_fish: int = len(self.fish)

        new_fish: int = (initial_fish // 2) * 4

        while new_fish > 0:
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        return None

    def view_river(self) -> None:
        """Prints the state the river is in"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Moves forward one week in the simulation"""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Removes specified amount of fish frm the river"""
        i: int = 0

        while i < amount:
            self.fish.pop(i)
        return None
