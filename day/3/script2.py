import re

from script1 import calculate_muls


def get_input(file_name: str) -> list[list[int]]:
    with open(file_name, "r") as f:
        list_of_muls = []
        is_enabled = True
        file = "".join(f.readlines())
        for i in range(len(file)):
            if file.startswith("do()"):
                is_enabled = True
            elif file.startswith("don't()"):
                is_enabled = False

            if is_enabled:
                dziengiel = re.findall(r"^mul\(\d{1,3},\d{1,3}\)", file)
                for mul in dziengiel:
                    mul = mul[4:-1]
                    mul = mul.split(",")
                    new_mul = []
                    for n in mul:
                        new_mul.append(int(n))
                    list_of_muls.append(new_mul)

            file = file[1:]

    return list_of_muls


if __name__ == "__main__":
    muls = get_input("input")
    print(calculate_muls(muls))
