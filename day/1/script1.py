def get_input(file_name: str) -> list[list[int]]:
    with open(file_name, 'r') as f:
        row_1 = []
        row_2 = []
        for line in f:
            line = line.split("   ")
            row_1.append(int(line[0]))
            row_2.append(int(line[1]))
        all_rows = [row_1, row_2]
    return all_rows


def calculate_distance(list_of_rows: list[list[int]]) -> int:
    row_1 = list_of_rows[0]
    row_2 = list_of_rows[1]
    row_1 = sorted(row_1)
    row_2 = sorted(row_2)
    distance = 0
    for i in range(len(row_1)):
        distance += abs(row_1[i] - row_2[i])
    return distance


if __name__ == "__main__":
    input_data = get_input("input")
    print(calculate_distance(input_data))
