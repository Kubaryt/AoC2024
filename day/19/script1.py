def get_input(file_name: str) -> dict[str, list[str]]:
    with open(file_name, "r") as file:
        lines = file.read()
        available_towels = lines.split("\n")[0].strip().split(", ")
        combinations = lines.split("\n")[1]

    return {"available_towels": available_towels, "combinations": combinations}


def check_combinations(towels_and_combinations: dict[str, list[str]]) -> int:
    for combination in towels_and_combinations["combinations"]:
