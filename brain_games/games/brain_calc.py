from random import randint, choice
from operator import add, sub, mul


DESCRIPTION = "What is the result of the expression?"


def game() -> tuple:
    num1, num2 = randint(1, 10), randint(1, 10)
    symbol, correct_answer = select_operation(num1, num2)
    question = f'{num1} {symbol} {num2}'
    return (question, correct_answer)


def select_operation(num1: int, num2: int):
    operations = [
        ['+', add(num1, num2)],
        ['-', sub(num1, num2)],
        ['*', mul(num1, num2)]
    ]
    return list(choice(operations))
