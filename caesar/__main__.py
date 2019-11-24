#!/usr/bin/env python

from sys import argv, exit
from .Caesar import Caesar
from pathlib import Path

def load_file(path: Path) -> str:
    with open(path, 'r') as open_file:
        return open_file.read()

def show_help() -> None:
    print("Caesar - et tu, brutus?\n\n")
    print("USAGE: python -m caesar [OPTIONS]")
    print("--encrypt [STRING]: encrypts word with default key\n")
    print("--decrypt [STRING]: decrypts word with default key\n")
    print("--key [INTEGER]: set custom key for encryption or decryption\n")
    print("--file [PATH]: fetches file content for input\n")
    print("--output [PATH]: sends output to given file\n")

if __name__ == "__main__":

    caesar: Caesar = Caesar()
    key: int = 2
    path: Path = None
    word: str = None
    multiplier: int = 0

    if '-h' in argv or '--help' in argv:
        show_help()
        exit()

    try:
        for index, argument in enumerate(argv):
            if argument == '--key' or argument == '-k':
                key = int(argv[index + 1])
            if argument == '--file' or argument == '-f':
                word = load_file(Path(argv[index + 1]))
            if argument == '--output' or argument == '-o':
                path = Path(argv[index + 1])

        for index, argument in enumerate(argv):
            if (argument == '--encrypt' or argument == '-e'):
                if word is None:
                    word = caesar.encrypt(argv[index + 1], key)
                multiplier = 1
            elif (argument == '--decrypt' or argument == '-d'):
                if word is None:
                    word = caesar.encrypt(argv[index + 1], -key)
                multiplier = -1
        
        if path is not None and word is not None:
            word = caesar.encrypt(word, key * multiplier)
            caesar.to_file(word, path)
        elif path is None and word is not None:
            word = caesar.encrypt(word, key * multiplier)
            print(word)
        else:
            print(word)

    except NameError:
        print("You should pass a key for encrypting ou decrypting a string, the key is an integer with range from 1 to 13.")
    except IndexError:
        print("Key should be in range 1..13")