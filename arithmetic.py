import random
import os

number_value = {
    "Right!": 1,
    "Wrong!": 0
}

level_description = {
    "1": "simple operations with numbers 2-9",
    "2": "integral squares of 11-29",
}

# write your code here
def basic_arithmetic_opp(first: str | int, operator, second: str | int):
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

def integral_squares_opp(basis_value: str | int):
    try:
        basis_value = int(basis_value) if type(basis_value) is not int else basis_value
        return basis_value ** 2
    except ValueError:
        return "Incorrect format."

def prepare_math_operation(first_boundary_left: str | int = 2,
                           first_boundary_right: str | int = 9,
                           second_boundary: str | int | None = None,
                           operators: tuple = ("+", "-", "*"),
                           level: str = "1"):

    first_param = random.randint(first_boundary_left, first_boundary_right)

    if level == "1":
        operator = random.choice(operators)
        second_param = random.randint(2, second_boundary)
        return (
            f"{first_param} {operator} {second_param}", str(basic_arithmetic_opp(first_param, operator, second_param)),
        )
    elif level == "2":
        return first_param, str(integral_squares_opp(first_param))
    else:
        return "Incorrect format."


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


def single_turn(msg_to_point: dict[str, int], level: str) -> int:
    if level == "1":
        operation, result = prepare_math_operation(first_boundary_left=2, first_boundary_right=9, second_boundary=9,
                                                   operators=("+", "-", "*"), level=level)
    else:
        operation, result = prepare_math_operation(first_boundary_left=11, first_boundary_right=29, level=level)

    print(operation)
    user_choice = input()

    answer_evaluation = check_user_input(user_choice, result)
    print(answer_evaluation)

    while answer_evaluation == "Incorrect format.":
        user_choice = input()
        answer_evaluation = check_user_input(user_choice, result)
        print(answer_evaluation)

    return msg_to_point.get(answer_evaluation)


def save_in_file_optional(user_points: int, level: str):
    print("Your mark is 4/5. Would you like to save the result? Enter yes or no.")

    user_choice = input()

    if user_choice.lower() == "yes" or user_choice.lower() == "y":
        name = input("What is your name?\n")
        with open("results.txt", ("a" if os.path.exists("results.txt") else "w")) as file:
            file.write(f"{name}: {user_points}/5 in level {level} ({level_description[level]})\n")
        print('The results are saved in "results.txt".')
    return None



if __name__ == '__main__':
    print("Which level do you want? Enter a number:",
          f"1 - {level_description['1']}",
          f"2 - {level_description['2']}",
          sep="\n")

    chosen_level = input()
    
    while chosen_level != "1" and chosen_level != "2":
        print("Incorrect format.")
        chosen_level = input()

    points = 0

    for turn in range(5):
        points += single_turn(number_value, level=chosen_level)

    print(f"Your mark is {points}/5.")

    save_in_file_optional(points, chosen_level)
