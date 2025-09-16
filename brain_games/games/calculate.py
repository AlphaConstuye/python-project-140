from random import randint, choice


def Question_operate():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operadores = choice(["+","-", "*"])

    if operadores == "+":
        correct_answer = num1 + num2
    elif operadores == "-":
          correct_answer = num1 - num2
    elif operadores == "*":
          correct_answer = num1 * num2

    print(f'Question: {num1} {operadores} {num2}')
    return correct_answer

def answer(correct_answer):
    user_input = input("Your answer: ")
    try:
        user_answer = int(user_input)
    except ValueError:
        # entrada no convertible a entero → considera respuesta incorrecta
        print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
        return False

    if user_answer == correct_answer:
        print("Correct!")
        return True

    print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
    return False

