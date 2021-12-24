from typing import Dict

from src.util import *

instruction_lines = [line.split() for line in Parser.from_file(INPUT).to_lines()]


def calculate(digit_nr: int, prev_output: Dict[int, int]) -> Dict[int, int]:
    print(f"Calculating for digit: {digit_nr} with prev_output size: {len(prev_output)}")
    instructions = instruction_lines[(digit_nr - 1) * 18 + 1:digit_nr * 18]
    key_addition = instructions[4][2]
    should_split = key_addition[0] == "-"
    next_output = {}
    for prev_answer, prev_number in prev_output.items():
        for next_digit in range(1, 10):
            register = {"w": next_digit, "x": 0, "y": 0, "z": prev_answer}
            for instruction in instructions:
                action = instruction[0]
                a = instruction[1]
                b = instruction[2]
                if "wxyz".__contains__(b):
                    b = register[b]
                else:
                    b = int(b)
                if action == "add":
                    register[a] = register[a] + b
                elif action == "mul":
                    register[a] = register[a] * b
                elif action == "div":
                    register[a] = int(register[a] / b)
                elif action == "mod":
                    register[a] = register[a] % b
                elif action == "eql":
                    register[a] = 1 if register[a] == b else 0
            next_answer = register["z"]
            next_number = prev_number * 10 + next_digit
            next_output[next_answer] = next_number

    if digit_nr == 14:
        return next_output
    elif should_split:
        min_val = min(next_output.keys())
        next_output = {answer: number for answer, number in next_output.items() if answer < min_val * 10}
    return calculate(digit_nr + 1, next_output)


answers = calculate(1, {0: 0})
print(answers)
print(len(answers))
