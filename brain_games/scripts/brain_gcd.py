#!/usr/bin/env python3
import brain_games.game_engine as game_engine
import brain_games.games.brain_gcd as brain_gcd_game


def main():
    game_engine.play(brain_gcd_game)


if __name__ == "__main__":
    main()
