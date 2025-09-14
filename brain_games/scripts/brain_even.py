#!/usr/bin/env python3

import sys
from brain_games.games import even

def greet_and_get_name() -> str:
    print('Welcom to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def main():
    name = greet_and_get_name()
    print('Answer "yes" if the number is even, otherwise anser "no".')

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
