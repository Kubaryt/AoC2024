class LabMap:
    rows = list
    columns = list
    guard_position = [int, int, str]
    # guard_position[0] - column number,
    # guard_position[1] - row number,
    # guard_position[2] - direction
    def __init__(self):
        self.rows = []
        self.columns = []
        self.guard_position = [0, 0, ""]

    def __str__(self):
        return f"rows: {self.rows}\ncolumns: {self.columns}\nguard_position: {self.guard_position}"

def get_input(file_name:str) -> LabMap:
    with open(file_name, "r") as file:
        lab_map = LabMap()
        i = 0
        for row in file:
            row = row.strip()
            lab_map.rows.append(row)
            if row.find("^") != -1:
                lab_map.guard_position = [row.index("^"), i, "^"]
            i += 1
        for i in range(len(lab_map.rows)):
            column = ""
            for row in lab_map.rows:
                column += row[i]
            lab_map.columns.append(column)
        print(lab_map)
        print(len(lab_map.columns))
        print(len(lab_map.rows))
        return lab_map


def forsee_guard_path(lab_map:LabMap) -> list[(int, int)]:
    places_visited = []
    for i in range(len(lab_map.columns) * len(lab_map.rows)):
        match lab_map.guard_position[2]:
            case "^":
                print(lab_map.guard_position)
                for char in lab_map.columns[lab_map.guard_position[0]][lab_map.guard_position[1]::-1]:
                    if char == "#":
                        lab_map.guard_position[2] = ">"
                        lab_map.guard_position[1] += 1
                        break
                    else:
                        try:
                            places_visited.index((lab_map.guard_position[0], lab_map.guard_position[1]))
                        except ValueError:
                            places_visited.append((lab_map.guard_position[0], lab_map.guard_position[1]))
                        lab_map.guard_position[1] -= 1
            case ">":
                print(lab_map.guard_position)
                for char in lab_map.rows[lab_map.guard_position[1]][lab_map.guard_position[0]:]:
                    if char == "#":
                        lab_map.guard_position[2] = "v"
                        lab_map.guard_position[0] -= 1
                        break
                    else:
                        try:
                            places_visited.index((lab_map.guard_position[0], lab_map.guard_position[1]))
                        except ValueError:
                            places_visited.append((lab_map.guard_position[0], lab_map.guard_position[1]))
                        lab_map.guard_position[0] += 1
            case "v":
                print(lab_map.guard_position)
                for char in lab_map.columns[lab_map.guard_position[0]][lab_map.guard_position[1]:]:
                    if char == "#":
                        lab_map.guard_position[2] = "<"
                        lab_map.guard_position[1] -= 1
                        break
                    else:
                        try:
                            places_visited.index((lab_map.guard_position[0], lab_map.guard_position[1]))
                        except ValueError:
                            places_visited.append((lab_map.guard_position[0], lab_map.guard_position[1]))
                        lab_map.guard_position[1] += 1
            case "<":
                print(lab_map.guard_position)
                for char in lab_map.rows[lab_map.guard_position[1]][lab_map.guard_position[0]::-1]:
                    print(char)
                    if char == "#":
                        lab_map.guard_position[2] = "^"
                        lab_map.guard_position[0] += 1
                        break
                    else:
                        try:
                            places_visited.index((lab_map.guard_position[0], lab_map.guard_position[1]))
                        except ValueError:
                            places_visited.append((lab_map.guard_position[0], lab_map.guard_position[1]))
                        lab_map.guard_position[0] -= 1
    return places_visited


if __name__ == "__main__":
    lab_map = get_input("input")
    places_visited = forsee_guard_path(lab_map)
    print(len(places_visited))
