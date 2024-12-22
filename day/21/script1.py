numerical_keypad = {
    "rows": ["789", "456", "123", " 0A"],
    "starting_position": (3, 2)
}

directional_keypad = {
    "rows": [" ^A", "<v>"]
    "starting_position": (0, 2)
}


def get_input(file_name: str) -> list[str]:
    with open(file_name, "r") as file:
        codes = file.read().split("\n")

    return codes


def find_code_route(code: str) -> list[str]:
    dp = {}
    for char in code:
        find_char_route(char, directional_keypad["starting_position"], dp)


def find_char_route(char: str, pos: tuple[int, int], dp: dict[str, int], keypad_type: str="directional") -> (list[str], dict[str, int]):
    while True:
        pass
