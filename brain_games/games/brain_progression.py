#!/usr/bin/env python3
from random import randint


DESCRIPTION = "What number is missing in the progression?"


def game() -> tuple:
    correct_answer, progression = gen_task()
    question = progression
    return (question, correct_answer)


def gen_task() -> tuple:
    start, count, step = randint(1, 25), randint(5, 10), randint(2, 10)
    stop = start + count * step
    miss_index = randint(1, count - 1)
    task = [i for i in range(start, stop, step)]
    miss, task[miss_index] = task[miss_index], '..'
    task = format_task(task)
    return (miss, task)


def format_task(task: list) -> str:
    res = ''
    for val in task:
        res += f'{val} '
    return res
