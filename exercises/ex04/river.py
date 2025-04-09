"""File to define River class."""

__author__: str = "730648844"

# Importing Fish and Bear
from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """River that will keep track of population and events."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the ages of fish and bears, and removes old one from the list."""
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
        """Decides if bears will eat or not depending on the amount of fish."""
        # Check if there are enough fish left for the bears, and they will eat
        # if there are enough
        for b in self.bears:
            if len(self.fish) >= 5:
                b.eat(3)
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Checks if bears have starved and removes if they have."""
        # List to keep track of how many bears are hungry
        hungry_bears: list[Bear] = []

        # Will check if any bear's hunger score is less than 0, and will keep track of
        # those who are
        for b in self.bears:
            if b.hunger_score < 0:
                hungry_bears.append(b)

        # Will remove bears from the river if they are on the hungry list from before
        for b in self.bears:
            if b in hungry_bears:
                self.bears.remove(b)
        return None

    def repopulate_fish(self):
        """Repopulates the fish population in the river."""
        # Finds out who many fish are in the river first
        initial_fish: int = len(self.fish)

        # Calculates how many new fish will appear
        new_fish: int = (initial_fish // 2) * 4

        # Adds the new fish to the River
        while new_fish > 0:
            self.fish.append(Fish())
            new_fish -= 1
        return None

    def repopulate_bears(self):
        """Repopulates the bear population."""
        # The initial bear population
        initial_bears: int = len(self.bears)

        # Adds the new bears to the list
        new_bears: int = initial_bears // 2

        # Adds the new bears to the River
        while new_bears > 0:
            self.bears.append(Bear())
            new_bears -= 1
        return None

    def view_river(self) -> None:
        """Prints the state the river is in."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
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
        """Moves forward one week in the simulation."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Removes specified amount of fish frm the river."""
        # Counter
        i: int = 0

        # While there are enough fish in the river, that amount will be removed
        while i < amount and len(self.fish):
            self.fish.pop(0)
            i += 1
        return None
