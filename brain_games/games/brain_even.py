#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game() -> tuple:
    num = randint(1, 100)
    correct_answer = is_even(num)
    question = f'{num}'
    return (question, correct_answer)


def is_even(num: int) -> str:
    if num % 2 == 0:
        return 'yes'
    return 'no'
