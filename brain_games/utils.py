#!/usr/bin/env python3
import prompt
import brain_games.cli as cli


def game_start(game, message: str):
    player_name = welcome_user()
    print(message)
    is_lose = False
    games_count = 3
    while games_count != 0 and not is_lose:
        question, correct_answer = game()
        result = game_round(question, correct_answer)
        is_lose = result[0]
        if not is_lose:
            print('Correct!')
            games_count -= 1
    if not result[0]:
        print_good_result(player_name)
    else:
        print_bad_result(player_name, *result[1:])


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
