#!/usr/bin/env python3
import prompt
import brain_games.cli as cli


def game_round(question: str, correct_answer) -> tuple:
    print(f'Question: {question}')
    answer = prompt.string('Your answer: ')
    is_lose = not check_answer(str(answer), str(correct_answer))
    return (is_lose, answer, correct_answer)


def welcome_user():
    print("Welcome to the Brain Games!")
    return cli.welcome_user()


def print_good_result(player_name: str):
    print(f"Congratulations, {player_name}!")


def print_bad_result(player_name: str, ans: str, cor_ans: str):
    print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'.")
    print(f"Let's try again, {player_name}!")


def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer == correct_answer
