#!/usr/bin/env python3

import sys

from brain_games.cli import welcome_user
from brain_games.games import even


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    round_to_win = 3

    for _ in range(round_to_win):
        number, correct_answer = even.generate_question()
        print(f'Question: {number}')
        user_answer = input('Your answer: ').strip().lower()

        if user_answer not in ('yes', 'no') or not even.is_correct(user_answer, correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            sys.exit(1)

        print('Correct!')

    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
