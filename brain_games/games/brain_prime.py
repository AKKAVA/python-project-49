#!/usr/bin/env python3
from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game() -> tuple:
    num = randint(2, 100)
    question = str(num)
    correct_answer = is_prime(num)
    return (question, correct_answer)


def is_prime(num: int) -> str:
    count = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            count += 1
    if count > 1:
        return 'no'
    return 'yes'
