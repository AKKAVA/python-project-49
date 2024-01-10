#!/usr/bin/env python3
import brain_games.cli as cli


PLAYER_NAME = ''


def main():
    global PLAYER_NAME
    print("Welcome to the Brain Games!")
    PLAYER_NAME = cli.welcome_user()


def print_good_result():
    print(f"Congratulations, {PLAYER_NAME}!")


def print_bad_result(ans: str, cor_ans: str):
    print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'.")
    print(f"Let's try again, {PLAYER_NAME}!")


if __name__ == "__main__":
    main()
