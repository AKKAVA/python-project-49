#!/usr/bin/env python3
import brain_games.game_engine as game_engine
import brain_games.games.brain_progression as brain_progression_game


def main():
    game_engine.play(brain_progression_game)


if __name__ == "__main__":
    main()
