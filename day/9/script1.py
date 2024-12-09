def get_input(file_name: str) -> list[str | int]:
    with open(file_name) as file:
        blocks = []
        id = 0
        for i, char in enumerate(file.readline().strip()):
            if i % 2 == 0:
                for j in range(int(char)):
                    blocks.append(id)
                id += 1
            else:
                for j in range(int(char)):
                    blocks.append(".")

        return blocks


def create_map(_blocks: list[str | int]) -> list[int]:
    _file_system_map = _blocks
    dots_count = _blocks.count(".")
    for block in _blocks[::-1]:
        if block == ".":
            continue
        else:
            try:
                _file_system_map[_file_system_map.index(".")] = block
            except ValueError:
                break


    return _file_system_map[:-dots_count]


def calculate_checksum(_file_system_map: list[int]) -> int:
    total = 0
    for i, char in enumerate(_file_system_map):
        total += i * int(char)

    return total


if __name__ == "__main__":
    blocks = get_input("input")
    file_system_map = create_map(blocks)
    print(calculate_checksum(file_system_map))
