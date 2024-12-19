def get_input(file_name: str) -> dict[str, list[str]]:
    with open(file_name, "r") as file:
        lines = file.read()
        available_towels = lines.split("\n\n")[0].strip().split(", ")
        combinations = lines.split("\n\n")[1].split("\n")

    return {"available_towels": available_towels, "combinations": combinations}


def check_combinations(towels_and_combinations: dict[str, list[str]], is_part2: bool=False) -> int:
    dp = {}
    result = 0
    for combination in towels_and_combinations["combinations"]:
        is_valid = check(combination, dp, towels_and_combinations["available_towels"])
        if is_valid >= 1 and not is_part2:
            result += 1
        if is_part2:
            result += is_valid

    return result


def check(combination: str, dp: dict[str, bool], available_towels: list[str]) -> (dict[str, int], int):
    if dp.get(combination, None) is not None:
        return dp[combination]

    if combination == "":
        return 1

    result = 0
    for towel in available_towels:
        if combination.startswith(towel):
            result += check(combination[len(towel):], dp, available_towels)

    dp[combination] = result
    return result


def test():
    task_input = get_input("test_input")
    result = check_combinations(task_input)
    assert result == 6
    result = check_combinations(task_input, True)
    assert result == 16


def solve():
    task_input = get_input("input")
    result = check_combinations(task_input)
    print(result)
    result = check_combinations(task_input, True)
    print(result)

if __name__ == "__main__":
    test()
    solve()
