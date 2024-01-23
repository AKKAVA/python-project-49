from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game() -> tuple:
    num = randint(1, 100)
    if is_even(num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f'{num}'
    return (question, correct_answer)


def is_even(num: int) -> bool:
    return num % 2 == 0
