import copy
from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    NONE = auto()


def get_input(file_name: str) -> dict[str, list[list[int]] | list[int, int]]:
    with open(file_name, "r") as file:
        map = {
            "rows": [],
            "trailheads": []
        }
        y = 0
        for row in file:
            row = row.strip()
            map["rows"].append([int(char) for char in row])
            if row.find("0") != -1:
                x = 0
                for char in row:
                    if char == "0":
                        map["trailheads"].append([x, y])
                    x += 1
            y += 1
    return map


def validate_trailheads(map: dict[str, list[list[int]] | list[int, int]]) -> int:
    total = 0
    for trailhead in map["trailheads"]:
        reached_nines = []
        possible_directions = []
        if trailhead[0] != 0:
            try:
                if map["rows"][trailhead[1]][trailhead[0] - 1] == 1:
                    possible_directions.append(Direction.LEFT)
            except IndexError:
                pass
        try:
            if map["rows"][trailhead[1]][trailhead[0] + 1] == 1:
                possible_directions.append(Direction.RIGHT)
        except IndexError:
            pass
        if trailhead[1] != 0:
            try:
                if map["rows"][trailhead[1] - 1][trailhead[0]] == 1:
                    possible_directions.append(Direction.UP)
            except IndexError:
                pass
        try:
            if map["rows"][trailhead[1] + 1][trailhead[0]] == 1:
                possible_directions.append(Direction.DOWN)
        except IndexError:
            pass
        for direction in possible_directions:
            additonal_total, reached_nines = find_route(map, direction, pos=[trailhead[0], trailhead[1]], current_height=0, reached_nines=reached_nines)
            total += additonal_total
    return total


def find_route(map: dict[str, list[list[int]] | list[int, int]], direction: Direction, pos: list[int, int], current_height: int, reached_nines: list) -> (int, list):
    total = 0
    possible_directions = []
    match direction:
        case Direction.LEFT:
            pos[0] -= 1
        case Direction.RIGHT:
            pos[0] += 1
        case Direction.UP:
            pos[1] -= 1
        case Direction.DOWN:
            pos[1] += 1
    current_height += 1
    if current_height == 9:
        if pos not in reached_nines:
            reached_nines.append(pos)
            total += 1
        return total, reached_nines
    if pos[0] != 0:
        try:
            if map["rows"][pos[1]][pos[0] - 1] == current_height + 1:
                possible_directions.append(Direction.LEFT)
        except IndexError:
            pass
    try:
        if map["rows"][pos[1]][pos[0] + 1] == current_height + 1:
            possible_directions.append(Direction.RIGHT)
    except IndexError:
        pass
    if pos[1] != 0:
        try:
            if map["rows"][pos[1] - 1][pos[0]] == current_height + 1:
                possible_directions.append(Direction.UP)
        except IndexError:
            pass
    try:
        if map["rows"][pos[1] + 1][pos[0]] == current_height + 1:
            possible_directions.append(Direction.DOWN)
    except IndexError:
        pass
    for _direction in possible_directions:
        temp_pos = copy.deepcopy(pos)
        additional_total, reached_nines = find_route(map, _direction, temp_pos, current_height, reached_nines)
        total += additional_total
    return total, reached_nines


def test():
    map = get_input("test_input")
    total = validate_trailheads(map)
    assert total == 36


def solve():
    map = get_input("input")
    total = validate_trailheads(map)
    print(total)

if __name__ == "__main__":
    test()
    solve()