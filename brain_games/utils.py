import prompt
import brain_games.cli as cli


def welcome_user():
    print("Welcome to the Brain Games!")
    return cli.welcome_user()


def user_answer(question: str):
    return prompt.string(f'Question: {question}\nYour answer: ')
