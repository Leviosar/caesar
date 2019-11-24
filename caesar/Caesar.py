from random import randint
from pathlib import Path

class Caesar:
    def __init__(self):
        self.letters = [chr(letter) for letter in range(97, 123)]

    def encrypt(self, word: str, key: int) -> str:
        output = ''
        for letter in word:
            try:
                output += self.letters[self.calculate_position(self.letters.index(letter), key)]
            except ValueError:
                output += letter
            except IndexError:
                output += self.letters[self.calculate_position(self.letters.index(letter) - 1, key)]
        return output

    def calculate_position(self, position: int, key: int) -> int:
        if (position + key) > len(self.letters) - 1:
            overflow: int = (len(self.letters) - (position + key)) * -1
            return overflow
        else:
            return position + key

    def to_file(self, word: str, path: Path) -> None:
        with open(path, 'w') as write_file:
            write_file.write(word)