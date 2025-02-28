"""In class coding test"""


def check_first_letter(word: str, letter: str) -> str:
    """checks if the word starts with the given first letter"""
    if word[0] == letter:
        return "Match!"
    else:
        return "No match!"


def pack(df: float) -> str:
    """Packing advice."""
    if df > 0.0 and df <= 50.0 and df < 75.0:
        return "Warm Jacket"
    else:
        if df <= 0.0:
            return "Stay inside"
        else:
            if df >= 75.0:
                return "Short Sleeves"
            else:
                return "Long Sleeves"
