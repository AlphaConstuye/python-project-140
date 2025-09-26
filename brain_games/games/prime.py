from random import randint


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def Question_operate():
    numero = randint(1, 20)
    correct_answer = "yes" if is_prime(numero) else "no"

    print(f'Question: {numero}')
    return correct_answer


def answer(correct_answer):
    user_input = input("Your answer:(yes/no): ").lower().strip()
    if user_input == correct_answer:
        print("Correct!")
        return True

    else:
        print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False
