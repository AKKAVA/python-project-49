#!/usr/bin/env python3
import brain_games.cli as cli


def game_start(game):
    player_name = welcome_user()
    results = game()
    if not results[0]:
        print_good_result(player_name)
    else:
        print_bad_result(player_name, *results[1:])


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
