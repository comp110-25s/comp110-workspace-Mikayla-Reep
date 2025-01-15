"""My first exercise in COMP110!"""

__author__ = "730648844"


def greet(name: str) -> str:
    """A welcoming fist function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("What is your name? ")))

# Reflection Question 1: Expresisons can be used as arguments instead of
# str literals. For example, you could create a new variable like name
# and do name = "Mikayla" and then do greet(name) to call the function.
# This would result in the same output as greet(name="Mikayla") without
# only using a str literal.

# Reflection Question 2: Yes, you can use the resulting value of a call
# to greet as an argument in another call to greet. This will result in
# the name argument being "Hello, name!", so when used again it will be
# "Hello, Hello, name!!".
