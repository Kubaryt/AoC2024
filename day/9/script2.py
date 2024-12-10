import copy


def get_input(file_name: str) -> list[tuple[str, int] | tuple[int, int]]:
    with open(file_name) as file:
        _blocks = []
        id = 0
        block = ""
        dots = ""

        for i, char in enumerate(file.readline().strip()):
            if i % 2 == 0:
                print(char)
                _blocks.append((id, int(char)))
                id += 1
            else:
                dots += "." * int(char)
                if dots != "":
                    _blocks.append((".", len(dots)))
                    dots = ""

        return _blocks


def create_map(
    _blocks: list[tuple[int, int] | tuple[str, int]],
) -> list[tuple[int, int] | tuple[str, int]]:
    _file_system_map = copy.deepcopy(_blocks)
    for i, block in enumerate(_blocks[::-1]):
        if block[0] == ".":
            continue
        else:
            try:
                dot_on_left = None
                if i == 0:
                    temp_map = _file_system_map
                    temp_map = temp_map[::-1]
                else:
                    temp_map = _file_system_map[::-1]
                    temp_map = temp_map[i:]
                for j, value in enumerate(temp_map[::-1]):
                    if value[0] == ".":
                        if value[1] >= block[1]:
                            dot_on_left = j
                            break
                if dot_on_left:
                    _file_system_map[_file_system_map.index(block)] = (".", block[1])
                    if _file_system_map[dot_on_left][1] == block[1]:
                        _file_system_map[dot_on_left] = block
                    else:
                        _file_system_map.insert(dot_on_left, block)
                        _file_system_map[dot_on_left + 1] = (
                            ".",
                            _file_system_map[dot_on_left + 1][1] - block[1],
                        )
            except IndexError:
                break

    return _file_system_map


def calculate_checksum(
    _file_system_map: list[tuple[int, int] | tuple[str, int]],
) -> int:
    total = 0
    i = 0
    for char in _file_system_map:
        if char[0] == ".":
            i += char[1]
            continue
        for _ in range(int(char[1])):
            total += i * char[0]
            i += 1

    return total


if __name__ == "__main__":
    blocks = get_input("input")
    print(blocks)
    file_system_map = create_map(blocks)
    print(file_system_map)
    print(calculate_checksum(file_system_map))
