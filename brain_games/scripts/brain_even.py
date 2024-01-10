#!/usr/bin/env python3
import prompt
from random import randint
import brain_games.utils as utils


def main():
    utils.game_start(game)


def game(games_count: int = 3) -> tuple:    # (result, player_answer, correct_answer)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_lose = False
    while games_count != 0 and not is_lose:
        num = randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ').lower()
        correct_answer = is_even(num)
        is_lose = not utils.check_answer(answer, correct_answer)
        if is_lose:
            return (is_lose, answer, correct_answer)
        print('Correct!')
        games_count -= 1
    return (is_lose, answer, correct_answer)


def is_even(num: int) -> str:
    if num % 2 == 0:
        return 'yes'
    return 'no'


if __name__ == '__main__':
    main()
