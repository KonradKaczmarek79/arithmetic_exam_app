import random
# import operator

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
    if answer == result:
        return "Right!"
    else:
        return "Wrong!"


if __name__ == '__main__':
    operation, result = prepare_math_operation(first_boundary=9, second_boundary=9, operators=("+", "-", "*"))
    print(operation)
    user_choice = input()

    print(check_user_input(user_choice, result))
