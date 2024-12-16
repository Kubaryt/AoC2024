import copy

from script1 import get_input, Direction


def validate_trailheads(map: dict[str, list[list[int]] | list[int, int]]) -> int:
    total = 0
    for trailhead in map["trailheads"]:
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
            additonal_total = find_route(map, direction, pos=[trailhead[0], trailhead[1]], current_height=0)
            total += additonal_total
    return total


def find_route(map: dict[str, list[list[int]] | list[int, int]], direction: Direction, pos: list[int, int], current_height: int) -> int:
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
        total += 1
        return total
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
        additional_total = find_route(map, _direction, temp_pos, current_height)
        total += additional_total
    return total


def test():
    map = get_input("test_input")
    total = validate_trailheads(map)
    assert total == 81


def solve():
    map = get_input("input")
    total = validate_trailheads(map)
    print(total)

if __name__ == "__main__":
    test()
    solve()
