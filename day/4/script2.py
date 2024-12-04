def part2(file_name: str) -> int:
    with open(file_name, "r") as file:
        file = file.readlines()
        all_xmas = 0
        for i in range(len(file) - 2):
            for j in range(len(file[i]) - 3):
                box = []
                for line in file[i:i+3]:
                    box.append(line[j:j+3])
                diagonal = box[0][0] + box[1][1] + box[2][2]
                if diagonal in ["MAS", "SAM"]:
                    for k in range(len(box)):
                        box[k] = box[k][::-1]
                    diagonal = box[0][0] + box[1][1] + box[2][2]
                    if diagonal in ["MAS", "SAM"]:
                        all_xmas += 1
    return all_xmas

if __name__ == "__main__":
    print(part2("input"))
