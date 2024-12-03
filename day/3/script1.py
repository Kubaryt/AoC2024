import re


def get_input(file_name: str) -> list[list[int]]:
    with open(file_name, "r") as f:
        list_of_muls = []
        for line in f:
            dziengiel = (re.findall(r"mul\(\d{1,3},\d{1,3}\)", line))
            for mul in dziengiel:
                mul = mul[4:-1]
                mul = mul.split(",")
                new_mul = []
                for n in mul:
                    new_mul.append(int(n))
                list_of_muls.append(new_mul)
    return list_of_muls


def calculate_muls(muls_list: list[list[int]]) -> int:
    total = 0
    for mul in muls_list:
        total += mul[0] * mul[1]
    return total


if __name__ == "__main__":
    muls = get_input("input")
    print(calculate_muls(muls))
