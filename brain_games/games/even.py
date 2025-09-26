from random import randint
from typing import Tuple

Min_number = 1
Max_number = 100


def generate_question() -> Tuple[int, str]:
    number = randint(Min_number, Max_number)
    correct = 'yes' if number % 2 == 0 else 'no'
    return number, correct


def is_correct(answer: str, correct_answer: str) -> bool:
    return answer == correct_answer
