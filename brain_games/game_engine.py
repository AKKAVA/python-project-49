import brain_games.utils as utils


GAMES_COUNT = 3


def play(game):
    player_name = utils.welcome_user()
    if game is None:
        return
    print(game.DESCRIPTION)
    is_lose = False
    count = 0
    while count != GAMES_COUNT and not is_lose:
        question, correct_answer = game.game()
        user_answer = utils.user_answer(question)
        is_lose = not check_answer(str(user_answer), str(correct_answer))
        if not is_lose:
            print('Correct!')
            count += 1
    if not is_lose:
        print_good_result(player_name)
    else:
        print_bad_result(player_name, user_answer, correct_answer)


def print_good_result(player_name: str):
    print(f"Congratulations, {player_name}!")


def print_bad_result(player_name: str, ans: str, cor_ans: str):
    print(f"'{ans}' is wrong answer ;(. Correct answer was '{cor_ans}'.")
    print(f"Let's try again, {player_name}!")


def check_answer(user_answer: str, correct_answer: str) -> bool:
    return user_answer == correct_answer
