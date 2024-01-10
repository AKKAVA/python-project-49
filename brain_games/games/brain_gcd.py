#!/usr/bin/env python3
from random import randint
from math import gcd
import brain_games.utils as utils


def main():
    utils.game_start(game)


def game(games_count: int = 3) -> tuple:
    print("Find the greatest common divisor of given numbers.")
    is_lose = False
    while games_count != 0 and not is_lose:
        num1, num2 = randint(1, 10), randint(1, 10)
        correct_answer = gcd(num1, num2)
        question = f'{num1} {num2}'
        round_result = utils.game_round(question, correct_answer)
        is_lose = round_result[0]
        if is_lose:
            return round_result
        print('Correct!')
        games_count -= 1
    return round_result


if __name__ == '__main__':
    main()
