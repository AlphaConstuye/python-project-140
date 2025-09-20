from brain_games.games.calculate import Question_operate, answer
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("What is the result of the expression?")

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

