import copy


def get_input(file_name: str) -> list[tuple[str, int] | tuple[int, int]]:
    with open(file_name) as file:
        _blocks = []
        id = 0

        for i, char in enumerate(file.readline().strip()):
            if i % 2 == 0:
                print(char)
                _blocks.append((id, int(char)))
                id += 1
            else:
                _blocks.append((".", len("." * int(char))))

        return _blocks


def create_map(
    _blocks: list[tuple[int, int] | tuple[str, int]],
) -> list[tuple[int, int] | tuple[str, int]]:
    _file_system_map = copy.deepcopy(_blocks)
    for i, block in enumerate(_blocks[::-1]):
        if block[0] == ".":
            continue
        else:
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
            if dot_on_left is not None:
                block_index = _file_system_map.index(block)
                if _file_system_map[block_index - 1][0] == "." or _file_system_map[block_index + 1][0] == ".":
                    if _file_system_map[block_index - 1][0] == ".":
                        while _file_system_map[block_index - 1][0] == ".":
                            _file_system_map[block_index] = (".", block[1] + _file_system_map[block_index - 1][1])
                            del _file_system_map[block_index - 1]
                            block_index -= 1
                    elif _file_system_map[block_index + 1][0] == ".":
                        while _file_system_map[block_index + 1][0] == ".":
                            _file_system_map[block_index] = (".", block[1] + _file_system_map[block_index + 1][1])
                            del _file_system_map[block_index + 1]
                else:
                    _file_system_map[block_index] = (".", block[1])
                if _file_system_map[dot_on_left][1] == block[1]:
                    # print("dziengiel", block)
                    _file_system_map[dot_on_left] = block
                else:
                    # print("dziengiel", block)
                    _file_system_map.insert(dot_on_left, block)
                    _file_system_map[dot_on_left + 1] = (
                        ".",
                        _file_system_map[dot_on_left + 1][1] - block[1],
                    )
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
            print(i, char[0], i * char[0])
            total += i * char[0]
            i += 1

    return total


if __name__ == "__main__":
    blocks = get_input("input")
    print(blocks)
    print("=====================================================")
    file_system_map = create_map(blocks)
    print(file_system_map)
    print(calculate_checksum(file_system_map))
