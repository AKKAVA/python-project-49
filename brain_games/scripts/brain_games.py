#!/usr/bin/env python3
import brain_games.cli as cli
from brain_games.scripts.brain_even import main as game_is_even


def main():
    print("Welcome to the Brain Games!")
    name = cli.welcome_user()
    result = game_is_even()
    print_result(result, name)


def print_result(result: bool, name: str):
    if result:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
