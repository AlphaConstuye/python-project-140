from brain_games.games.progression import Question_operate, answer


def greet_and_get_name() -> str:
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def main():
    name = greet_and_get_name()
    print("What number is missing in the progression?")

    correct_streak = 0
    rounds_to_win = 3

    while correct_streak < rounds_to_win:
        correct_answer = Question_operate()
        user_correct = answer(correct_answer)

        if user_correct:
            correct_streak += 1
        else:
            print(f"Let's try  again, {name}!")
            return

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()

