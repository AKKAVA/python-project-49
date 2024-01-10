#!/usr/bin/env python3
from random import randint, choice
import brain_games.utils as utils


def main():
    utils.game_start(game)


def game(games_count: int = 3) -> tuple:    # (result, player_answer, correct_answer)
    print("What is the result of the expression?")
    is_lose = False
    while games_count != 0 and not is_lose:
        num1, num2 = randint(1, 10), randint(1, 10)
        symbol, correct_answer = select_operation(num1, num2)
        question = f'{num1} {symbol} {num2}'
        round_result = utils.game_round(question, correct_answer)
        is_lose = round_result[0]
        if is_lose:
            return round_result
        print('Correct!')
        games_count -= 1
    return round_result


def select_operation(num1: int, num2: int):
    operations = [
        ['+', sum([num1, num2])],
        ['-', deduction(num1, num2)],
        ['*', multiplucation(num1, num2)]
    ]
    return list(choice(operations))


def deduction(num1, num2):
    return num1 - num2


def multiplucation(num1, num2):
    return num1 * num2


if __name__ == '__main__':
    main()
