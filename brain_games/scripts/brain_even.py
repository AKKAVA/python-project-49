#!/usr/bin/env python3
import prompt
from random import randint


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    is_win = game()
    return is_win


def game(games_count: int = 3) -> bool:
    is_not_lose = True
    while games_count != 0 and is_not_lose:
        num = randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ').lower()
        correct_answer = is_even(num)
        is_not_lose = check_answer(answer, correct_answer)
        print_result(is_not_lose, answer, correct_answer)
        games_count -= 1
    if not is_not_lose:
        return False
    return True


def print_result(flag: bool, ans: str, cor_ans: str):
    if flag:
        print('Correct!')
    else:
        print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'.")


def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer == correct_answer


def is_even(num: int) -> str:
    if num % 2 == 0:
        return 'yes'
    return 'no'


if __name__ == '__main__':
    print(main())
