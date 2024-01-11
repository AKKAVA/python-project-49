#!/usr/bin/env python3
from random import randint
from math import gcd
import brain_games.utils as utils


def main():
    message = "Find the greatest common divisor of given numbers."
    utils.game_start(game, message)


def game() -> tuple:
    num1, num2 = randint(1, 10), randint(1, 10)
    correct_answer = gcd(num1, num2)
    question = f'{num1} {num2}'
    return (question, correct_answer)


if __name__ == '__main__':
    main()
