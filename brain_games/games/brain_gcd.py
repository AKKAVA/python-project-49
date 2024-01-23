from random import randint
from math import gcd


DESCRIPTION = "Find the greatest common divisor of given numbers."


def game() -> tuple:
    num1, num2 = randint(1, 10), randint(1, 10)
    correct_answer = gcd(num1, num2)
    question = f'{num1} {num2}'
    return (question, correct_answer)
