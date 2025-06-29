import random

number_value = {
    "Right!": 1,
    "Wrong!": 0
}

# write your code here
def arithmetic(first: str | int, operator, second: str | int):
    try:
        first = int(first) if type(first) is not int else first
        second = int(second) if type(second) is not int else second
    except ValueError:
        return None
    else:
        if operator == '+':
            return first + second
        elif operator == '-':
            return first - second
        elif operator == '*':
            return first * second

def prepare_math_operation(first_boundary: str | int, second_boundary: str | int, operators: tuple = ("+", "-", "*")):
    operator = random.choice(operators)
    first_param = random.randint(2, first_boundary)
    second_param = random.randint(2, second_boundary)

    return (
        f"{first_param} {operator} {second_param}", str(arithmetic(first_param, operator, second_param)),
    )

def check_user_input(answer: str, result: str) -> str:
    try:
        answer = int(answer)
        result = int(result)
    except ValueError:
        return "Incorrect format."

    if answer == result:
        return "Right!"
    else:
        return "Wrong!"


def single_turn(msg_to_point: dict[str, int]):
    operation, result = prepare_math_operation(first_boundary=9, second_boundary=9, operators=("+", "-", "*"))
    print(operation)
    user_choice = input()

    answer_evaluation = check_user_input(user_choice, result)
    print(answer_evaluation)

    while answer_evaluation == "Incorrect format.":
        user_choice = input()
        answer_evaluation = check_user_input(user_choice, result)
        print(answer_evaluation)

    return msg_to_point.get(answer_evaluation)

if __name__ == '__main__':
    points = 0

    for turn in range(5):
        points += single_turn(number_value)

    print(f"Your mark is {points}/5.")
