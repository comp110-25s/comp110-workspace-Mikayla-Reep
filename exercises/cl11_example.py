"""Wordle like example for constants"""

SECRET: str = "turned"


def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    """Guessing the word"""
    if len(word) != len(secret):
        print("Words are different lenghts")
        return False
    else:
        if word[idx] != secret[idx]:
            print(f"{word[idx]} isn't the secret word's next letter")
            return False
        else:
            print(f"{word[idx]} is the next letter! Moving on...")
            if idx < len(secret) - 1:
                return guess_secret(word=word, secret=secret, idx=idx + 1)
            else:
                print(f"{word} is the secret word!")
                return True


print(guess_secret(word=input("What is your word? "), secret=SECRET))
