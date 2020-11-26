# -*- coding: utf-8 -*-
"""Tests for issue-01"""

LETTER_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----',
    ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': ' '
}

MORSE_TO_LETTER = {
    morse: letter
    for letter, morse in LETTER_TO_MORSE.items()
}


def encode(message: str) -> str:
    """
    Кодирует строку в соответствие с таблицей азбуки Морзе
    >>> encode('SOS')
    '... --- ...'
    >>> encode('ABBA') # doctest: +NORMALIZE_WHITESPACE
    '.- -...         -... .-'
    >>> encode('ABCDJSKAKADJADF') # doctest: +ELLIPSIS
    '.- -... -.-. -.............- .- -.. .--- .- -.. ..-.'
    >>> encode(1)
    Traceback (most recent call last):
      File "/Applications/PyCharm CE.app/Contents/helpers/pycharm/docrunner.py"
      , line 140, in __run
        compileflags, 1), test.globs)
      File "<doctest test_morse.encode[1]>", line 1, in <module>
        encode(1)
      File "/Users/aleksandrpolakov/PycharmProjects/avito_tests/test_morse.py"
      , line 42, in encode
        LETTER_TO_MORSE[letter] for letter in message
    TypeError: 'int' object is not iterable
    """
    encoded_signs = [
        LETTER_TO_MORSE[letter] for letter in message
    ]

    return ' '.join(encoded_signs)
