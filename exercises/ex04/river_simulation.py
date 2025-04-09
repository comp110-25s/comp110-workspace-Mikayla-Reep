"""File to run the simulation with fish, bears, and the river."""

__author__: str = "730648844"

# Importing River
from exercises.EX04.river import River

# Creating River Object
my_river = River(num_fish=10, num_bears=0)

# Viewing the river
my_river.view_river()

# Pass one week of time
my_river.one_river_week()

# Viewing again after one week
my_river.view_river()
