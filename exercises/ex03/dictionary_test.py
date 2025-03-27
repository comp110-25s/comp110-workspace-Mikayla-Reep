"""Tests for dictionary.py"""

__author__: str = "730648844"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len

# dictionaries to use
dict_empty: dict[str, str] = {}
dict_two_str_1: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
dict_two_str_1_inverted: dict[str, str] = {"z": "a", "y": "b", "x": "c"}
dict_two_str_2: dict[str, str] = {
    "park": "meadow",
    "bird": "flower",
    "honda": "cat",
    "mouth": "grey",
}
dict_two_str_2_inverted: dict[str, str] = {
    "meadow": "park",
    "flower": "bird",
    "cat": "honda",
    "grey": "mouth",
}
# strings to use
empty_list: list[str] = []
list_1: list[str] = ["jacket", "eyeball", "seven", "seven", "jacket"]
list_1_counted: dict[str, int] = {"jacket": 2, "eyeball": 1, "seven": 2}
list_2: list[str] = ["red", "blue", "red", "red", "red"]
list_2_counted: dict[str, int] = {"red": 4, "blue": 1}

# fav colors tests
fav_colors_1: dict[str, str] = {"a": "blue", "b": "red", "c": "blue", "d": "yellow"}
fav_colors_1_after: str = "blue"
fav_colors_tie: dict[str, str] = {
    "a": "blue",
    "b": "red",
    "c": "blue",
    "d": "yellow",
    "e": "yellow",
}
fav_colors_tie_after: str = "blue"

# bin_len
list_1_bin_len: dict[int, set[str]] = {
    6: {"jacket", "jacket"},
    7: {"eyeball"},
    5: {"seven", "seven"},
}
list_2_bin_len: dict[int, set[str]] = {3: {"red", "red", "red", "red"}, 4: {"blue"}}


# Tests for invert
def test_invert_use() -> None:
    """Testing the invert function when empty"""
    assert invert(dict_empty) == {}


def test_invert_use_1() -> None:
    """Testing the invert function with three inputs"""
    assert invert(dict_two_str_1) == dict_two_str_1_inverted


def test_invert_use_2() -> None:
    """Testing the invert function with 4 inputs"""
    assert invert(dict_two_str_2) == dict_two_str_2_inverted


# Tests for count
def test_count_empty() -> None:
    """Tests if count is given an empty list"""
    assert count(empty_list) == {}


def test_count_use_1() -> None:
    """Tests a use of count with normal input"""
    assert count(list_1) == list_1_counted


def test_count_use_2() -> None:
    """Tests a use of count with normal input"""
    assert count(list_2) == list_2_counted


# Tests for favorite color
def test_favorite_color_empty() -> None:
    """Tests favorite_color if given an empty dict"""
    assert favorite_color(dict_empty) == ""


def test_favorite_color_use_1() -> None:
    """Tests favorite_color with noraml inputs"""
    assert favorite_color(fav_colors_1) == fav_colors_1_after


def test_favorite_color_tie() -> None:
    """Tests favorite_color with noraml inputs and a tie for most mentioned"""
    assert favorite_color(fav_colors_tie) == fav_colors_tie_after


# Tests for bin_len
def test_bin_len_empty() -> None:
    """Tests bin_len if the list is empty"""
    assert bin_len(empty_list) == {}


def test_bin_len_use_1() -> None:
    """Test bin_len with normal inputs"""
    assert bin_len(list_1) == list_1_bin_len


def test_bin_len_use_2() -> None:
    """Test bin_len with normal inputs"""
    assert bin_len(list_2) == list_2_bin_len
