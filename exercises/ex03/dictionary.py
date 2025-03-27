"""Practice with dictionary functions"""

__author__: str = "730648844"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Turns the key into the value and vice versa"""

    # Creating new dict for output
    result: dict[str, str] = dict()

    # Goes through each set in the dict and reverese the key and value in result
    for key in a:
        if a[key] in result:
            raise KeyError("No duplicate keys")
        result[a[key]] = key
    return result


def count(input: list[str]) -> dict[str, int]:
    "Counts how many times the same string occures in the list"

    # New dictionary to built on to
    output: dict[str, int] = dict()

    # For loop will go through list, and add to output dict if new key, or add
    # 1 to values if duplicate key
    for item in input:
        if item in output:
            output[item] += 1
        else:
            output[item] = 1

    return output


def favorite_color(names_color: dict[str, str]) -> str:
    "Returns the most popular color"

    # Creating a list to store just colors
    color_list: list[str] = list()

    # Populates the color list
    for item in names_color:
        color_list.append(names_color[item])

    # Sends the color list to count to count how many of each color there is
    color_count: dict[str, int] = count(color_list)

    # Starter for highest int and str to find which color is mentioned the most
    highest_int: int = 0
    highest_str: str = ""

    # finds the highest number and associated color and stores highest as it looks
    # thorugh dict
    for item in color_count:
        if color_count[item] > highest_int:
            highest_int = color_count[item]
            highest_str = item

    return highest_str


def bin_len(words: list[str]) -> dict[int, set[str]]:
    "Groups words from a list into groups of the same length"

    # Dict that will have the str and its length
    word_length: dict[str, int] = {}
    binned: dict[int, set[str]] = {}

    # Will populate word_lengths
    for word in words:
        word_length[word] = len(word)
        print(word_length)

    # Will add a new set if there is no word of that length, and add to list is there
    # are other words of that length
    for word in word_length:
        if word_length[word] in binned:
            binned[word_length[word]].add(word)
        else:
            binned[word_length[word]] = set()
            binned[word_length[word]].add(word)
    return binned
