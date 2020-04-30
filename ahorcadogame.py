# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS =[
    'batman',
     'superman',
     'spiderman',
     'joker'
]

def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

def display_board(hidden_word, tries):
        print(IMAGES[tries])
        print('')
        print(hidden_word)
        print('---*---*---*---')


def run():
    word = random_word()
    hidden_word = ['-'] * len (word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(input('escoge una letra'))
    pass


if __name__ == '__main__':
     print('Bienvenidos a ahorcado jueguito')
     run()