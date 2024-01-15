#!/usr/bin/env python3
from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


def game() -> tuple:
    num1, num2 = randint(1, 10), randint(1, 10)
    symbol, correct_answer = select_operation(num1, num2)
    question = f'{num1} {symbol} {num2}'
    return (question, correct_answer)


def select_operation(num1: int, num2: int):
    operations = [
        ['+', sum([num1, num2])],
        ['-', deduction(num1, num2)],
        ['*', multiplucation(num1, num2)]
    ]
    return list(choice(operations))


def deduction(num1, num2):
    return num1 - num2


def multiplucation(num1, num2):
    return num1 * num2
