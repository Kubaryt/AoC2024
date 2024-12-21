from copy import deepcopy

def get_input(filename: str) -> dict[str, tuple[int, int] | list[str]]:
    with open(filename, 'r') as file:
        race_map = file.read().split('\n')
        start = None
        end = None
        for i, row in enumerate(race_map):
            if row.find("S") != -1:
                start = (row.find("S"), i)
            if row.find("E") != -1:
                end = (row.find("E"), i)
            if start is not None and end is not None:
                break

    return {"race_map": race_map, "start": start, "end": end}


def race_with_cheat(race_conditions: dict[str, tuple[int, int] | list[str]], minimal_cheat: int) -> int:
    visited_tiles = []
    pos = race_conditions["start"]
    counter = 0
    while True:
        x, y = pos
        skipped_tiles = 0
        try:
            if race_conditions["race_map"][y - 2][x] in [".", "E"] and race_conditions["race_map"][y - 1][x] == "#" and (x, y - 2) not in visited_tiles:
                skipped_tiles = get_path_without_cheating(race_conditions["race_map"], pos, (x, y - 2), deepcopy(visited_tiles))
                if skipped_tiles > minimal_cheat:
                    counter += 1
                    print(pos)
        except IndexError:
            pass
        try:
            if race_conditions["race_map"][y + 2][x] in [".", "E"] and race_conditions["race_map"][y + 1][x] == "#" and (x, y + 2) not in visited_tiles:
                skipped_tiles = get_path_without_cheating(race_conditions["race_map"], pos, (x, y + 2), deepcopy(visited_tiles))
                if skipped_tiles > minimal_cheat:
                    counter += 1
                    print(pos)
        except IndexError:
            pass
        try:
            if race_conditions["race_map"][y][x - 2] in [".", "E"] and race_conditions["race_map"][y][x - 1] == "#" and (x - 2, y) not in visited_tiles:
                skipped_tiles = get_path_without_cheating(race_conditions["race_map"], pos, (x - 2, y), deepcopy(visited_tiles))
                if skipped_tiles > minimal_cheat:
                    counter += 1
                    print(pos)
        except IndexError:
            pass
        try:
            if race_conditions["race_map"][y][x + 2] in [".", "E"] and race_conditions["race_map"][y][x + 1] == "#" and (x + 2, y) not in visited_tiles:
                skipped_tiles = get_path_without_cheating(race_conditions["race_map"], pos, (x + 2, y), deepcopy(visited_tiles))
                if skipped_tiles > minimal_cheat:
                    counter += 1
                    print(pos)
        except IndexError:
            pass
        if race_conditions["race_map"][y - 1][x] in [".", "E"] and (x, y - 1) not in visited_tiles:
            visited_tiles.append(pos)
            pos = (x, y - 1)
        elif race_conditions["race_map"][y + 1][x] in [".", "E"] and (x, y + 1) not in visited_tiles:
            visited_tiles.append(pos)
            pos = (x, y + 1)
        elif race_conditions["race_map"][y][x - 1] in [".", "E"] and (x - 1, y) not in visited_tiles:
            visited_tiles.append(pos)
            pos = (x - 1, y)
        elif race_conditions["race_map"][y][x + 1] in [".", "E"] and (x + 1, y) not in visited_tiles:
            visited_tiles.append(pos)
            pos = (x + 1, y)
        if pos == race_conditions["end"]:
            break

    return counter

def get_path_without_cheating(race_map: list[str], start: tuple[int, int], end: tuple[int, int], visited_tiles: list[tuple[int, int]]) -> int:
    pos = start
    counter = 0
    while True:
        x, y = pos
        if race_map[y - 1][x] in [".", "E"] and (x, y - 1) not in visited_tiles:
            visited_tiles.append(pos)
            pos = (x, y - 1)
        elif race_map[y + 1][x] in [".", "E"] and (x, y + 1) not in visited_tiles:
            visited_tiles.append(pos)
            pos = (x, y + 1)
        elif race_map[y][x - 1] in [".", "E"] and (x - 1, y) not in visited_tiles:
            visited_tiles.append(pos)
            pos = (x - 1, y)
        elif race_map[y][x + 1] in [".", "E"] and (x + 1, y) not in visited_tiles:
            visited_tiles.append(pos)
            pos = (x + 1, y)
        counter += 1
        if pos == end:
            break

    return counter


def test():
    test_input = get_input("test_input")
    counter = race_with_cheat(test_input, 10)
    print(counter)
    assert counter == 10
    print("Test passed.")


def test2():
    test_input = get_input("test_input")
    counter = race_with_cheat(test_input, 10)
    print(counter)
    assert counter == 129
    print("Test passed.")


def solve1():
    test_input = get_input("input")
    counter = race_with_cheat(test_input, 100)
    print(counter)


if __name__ == "__main__":
    test()
    solve1()