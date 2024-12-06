import copy

from script1 import get_input, LabMap, forsee_guard_path


def is_guard_looped(_lab_map: LabMap) -> bool:
    places_visited = []
    direction_dict = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0)
    }
    while True:
        previous_x = _lab_map.guard_position[0]
        previous_y = _lab_map.guard_position[1]
        _lab_map.guard_position[0] += direction_dict[_lab_map.guard_position[2]][0]
        _lab_map.guard_position[1] += direction_dict[_lab_map.guard_position[2]][1]
        if (_lab_map.guard_position[0], _lab_map.guard_position[1], _lab_map.guard_position[2]) in places_visited:
            return True

        if (_lab_map.guard_position[0] < 0 or _lab_map.guard_position[1] < 0
                or _lab_map.guard_position[0] >= len(_lab_map.columns) or _lab_map.guard_position[1] >= len(_lab_map.columns)):
            print(_lab_map.guard_position)
            return False

        if _lab_map.rows[_lab_map.guard_position[1]][_lab_map.guard_position[0]] == "#":
            match _lab_map.guard_position[2]:
                case "^":
                    _lab_map.guard_position[2] = ">"
                case ">":
                    _lab_map.guard_position[2] = "v"
                case "v":
                    _lab_map.guard_position[2] = "<"
                case "<":
                    _lab_map.guard_position[2] = "^"
            _lab_map.guard_position[0] = previous_x
            _lab_map.guard_position[1] = previous_y

        places_visited.append((_lab_map.guard_position[0], _lab_map.guard_position[1], _lab_map.guard_position[2]))

if __name__ == "__main__":
    lab_map = get_input("input")
    total = 0
    lab_map2 = copy.deepcopy(lab_map)
    for place in forsee_guard_path(lab_map2):
        j, i = place
        lab_map2 = copy.deepcopy(lab_map)
        if lab_map2.rows[i][j] not in ["^", "#"]:
            lab_map2.rows[i] = lab_map2.rows[i][:j] + "#" + lab_map2.rows[i][j+1:]
            lab_map2.columns[j] = lab_map2.columns[j][:i] + "#" + lab_map2.columns[j][i+1:]
            print(lab_map2.rows[i], i, j)
            if is_guard_looped(lab_map2):
                print(True)
                total += 1
    print(total)