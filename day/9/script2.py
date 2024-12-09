import copy
import re

from script1 import calculate_checksum


def get_input(file_name: str) -> (list[str | int], list[int]):
    with open(file_name) as file:
        blocks = []
        id = 0
        dots = ""
        _dots_indexes = []
        for i, char in enumerate(file.readline().strip()):
            if i % 2 == 0:
                if dots:
                    blocks.append(dots)
                    _dots_indexes.append(len(blocks) - 1)
                dots = ""
                for j in range(int(char)):
                    blocks.append(id)
                id += 1
            else:
                for j in range(int(char)):
                    dots += "."

        return blocks, _dots_indexes


def create_map(_blocks: list[str | int], _dots_indexes: list[int]) -> list[int]:
    _file_system_map = copy.deepcopy(_blocks)
    for block in _blocks[::-1]:
        if type(block) == str:
            continue
        else:
            try:
                if len(str(_file_system_map[dots_indexes[0]])) >= _file_system_map.count(str(block)):
                    print("dziengiel")
                    id_blocks = []
                    for _ in range(_file_system_map.count(str(block))):
                        id_blocks.append(block)
                    first_dot_index = _file_system_map.index(_blocks[dots_indexes.pop(0)])
                    for id_block in id_blocks:
                        _file_system_map.insert(first_dot_index, id_block)
                    print(_file_system_map[first_dot_index], first_dot_index)
                    print(_blocks)
                    del _file_system_map[first_dot_index]
            except IndexError:
                break

    return _file_system_map


if __name__ == "__main__":
    blocks, dots_indexes = get_input("input")
    print(blocks)
    file_system_map = create_map(blocks, dots_indexes)
    print(file_system_map)
    new_file_system_map = []
    for i in file_system_map:
        if type(i) == int:
            new_file_system_map.append(i)
    file_system_map = new_file_system_map
    print(calculate_checksum(file_system_map))