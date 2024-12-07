from itertools import product

def get_input(file_name: str) -> list[list[int, list[int]]]:
    all_equations = []
    with open(file_name) as file:
        for line in file:
            line = line.split(":")
            right_side = []
            for n in line[1].strip().split(" "):
                n = int(n)
                right_side.append(n)
            all_equations.append([int(line[0]), right_side])
    return all_equations


def solve(equations: list[list[int, list[int]]], uses_concatenation: bool=False) -> int:
    total = 0
    if uses_concatenation:
        operators = ["*", "+", "||"]
    else:
        operators = ["*", "+"]
    for equation in equations:
        if equation[0] == sum(equation[1]):
            total += equation[0]
            continue
        for value in product(*[operators] * (len(equation[1]) - 1)):
            n = equation[1][0]
            for i, symbol in enumerate(value):
                match symbol:
                    case "*":
                        n *= equation[1][i + 1]
                    case "+":
                        n += equation[1][i + 1]
                    case "||":
                        n = int(str(n) + str(equation[1][i + 1]))
            if n == equation[0]:
                total += n
                break

    return total


def part_one(equations: list[list[int, list[int]]]):
    print(solve(equations))


def part_two(equations: list[list[int, list[int]]]):
    print(solve(equations, uses_concatenation=True))

if __name__ == "__main__":
    equations = get_input("input")
    part_one(equations)
    part_two(equations)
