#!/usr/bin/env python3
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
        result = utils.game_round(question, correct_answer)
        is_lose = result[0]
        if not is_lose:
            print('Correct!')
            count += 1
    if not is_lose:
        utils.print_good_result(player_name)
    else:
        utils.print_bad_result(player_name, *result[1:])
