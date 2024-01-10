#!/usr/bin/env python3
from random import randint
import brain_games.utils as utils


def main():
    utils.game_start(game)


def game(games_count: int = 3) -> tuple:    # (result, player_answer, correct_answer)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_lose = False
    while games_count != 0 and not is_lose:
        num = randint(1, 100)
        correct_answer = is_even(num)
        question = f'{num}'
        round_result = utils.game_round(question, correct_answer)
        is_lose = round_result[0]
        if is_lose:
            return round_result
        print('Correct!')
        games_count -= 1
    return round_result


def is_even(num: int) -> str:
    if num % 2 == 0:
        return 'yes'
    return 'no'


if __name__ == '__main__':
    main()
