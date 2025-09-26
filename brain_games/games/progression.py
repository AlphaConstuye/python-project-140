from random import randint


def Question_operate():
    inicio = randint(1, 10)
    paso = randint(1, 5)
    longitud = 10
    progresion = [inicio + i * paso for i in range(longitud)]

    faltante_idx = randint(0, longitud - 1)

    correct_answer = progresion[faltante_idx]
    progresion[faltante_idx] = ".."

    print("Question:", " ".join(map(str, progresion)))
    return correct_answer


def answer(correct_answer):
    user_input = input("Your answer: ")
    try:
        user_answer = int(user_input)
    except ValueError:
        # entrada no convertible a entero → considera respuesta incorrecta
        print(
            f"'{user_input}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'."
        )
        return False

    if user_answer == correct_answer:
        print("Correct!")
        return True

    print(
        f"'{user_input}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'."
    )
    return False
