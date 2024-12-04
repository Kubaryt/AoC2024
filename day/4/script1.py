def part1(file_name: str) -> int:
    with open(file_name, "r") as file:
        file = file.readlines()
        all_xmas = 0
        for i in range(len(file)):
            line_xmas = file[i].count("XMAS") + file[i].count("SAMX")
            row_xmas = 0
            diagonal_xmas = 0
            if i - len(file) <= -4:
                next_four_lines = [file[i].strip(), file[i + 1].strip(), file[i + 2].strip(), file[i + 3].strip()]
                for j in range(len(next_four_lines[0])):
                    row = next_four_lines[0][j] + next_four_lines[1][j] + next_four_lines[2][j] + next_four_lines[3][j]
                    row_xmas += row.count("XMAS") + row.count("SAMX")
                for j in range(len(next_four_lines[0]) - 3):
                    diagonal = next_four_lines[0][j] + next_four_lines[1][j+1] + next_four_lines[2][j+2] + \
                               next_four_lines[3][j + 3]
                    diagonal_xmas += diagonal.count("XMAS") + diagonal.count("SAMX")
                for j in range(len(next_four_lines)):
                    next_four_lines[j] = next_four_lines[j][::-1]
                for j in range(len(next_four_lines[0]) - 3):
                    diagonal = next_four_lines[0][j] + next_four_lines[1][j+1] + next_four_lines[2][j+2] + \
                               next_four_lines[3][j + 3]
                    diagonal_xmas += diagonal.count("XMAS") + diagonal.count("SAMX")
            all_xmas += line_xmas + row_xmas + diagonal_xmas

    return all_xmas


if __name__ == "__main__":
    print(part1("input"))
