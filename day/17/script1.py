operands = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": "A",
    "5": "B",
    "6": "C"
}

def get_input(file_name: str) -> dict[str, int | str]:
    device_display = {
        "A": 0,
        "B": 0,
        "C": 0,
        "program": ""
    }
    with open(file_name, "r") as file:
        for line in file:
            if line.find("Register A") != -1:
                line = line.split(":")
                device_display["A"] = int(line[1].strip())
            elif line.find("Register B") != -1:
                line = line.split(":")
                device_display["B"] = int(line[1].strip())
            elif line.find("Register C") != -1:
                line = line.split(":")
                device_display["C"] = int(line[1].strip())
            elif line.find("Program") != -1:
                line = line.split(":")
                device_display["program"]= "".join(line[1].strip().split(","))

    return device_display


def execute_program(device_display: dict[str, int | str]) -> str:
    output = []
    i = 0
    while i < len(device_display["program"]):
        instruction = device_display["program"][i]
        instruction = int(instruction)
        combo_operand = operands[str(device_display["program"][i + 1])]
        literal_operand = int(device_display["program"][i + 1])
        match combo_operand:
            case "A":
                combo_operand = device_display["A"]
            case "B":
                combo_operand = device_display["B"]
            case "C":
                combo_operand = device_display["C"]
        match instruction:
            case 0:
                device_display["A"] = device_display["A"] // (2 ** combo_operand)
            case 1:
                device_display["B"] = device_display["B"] ^ int(literal_operand)
            case 2:
                device_display["B"] = combo_operand % 8
            case 3:
                if device_display["A"] != 0:
                    try:
                        if output[len(output) - 1] != device_display["program"][len(output) - 1]:
                            break
                    except IndexError:
                        break
                    i = literal_operand
                    continue
            case 4:
                device_display["B"] = device_display["B"] ^ device_display["C"]
            case 5:
                output.append(str(combo_operand % 8))
            case 6:
                device_display["B"] = device_display["A"] // (2 ** combo_operand)
            case 7:
                device_display["C"] = device_display["A"] // (2 ** combo_operand)
        i += 2

    return ",".join(output)



def test1():
    device_display = get_input("test_input1")
    print(device_display)
    program_output = execute_program(device_display)
    print(program_output)
    assert program_output == "4,6,3,5,6,3,5,2,1,0"


def test2():
    device_display = get_input("test_input2")
    device_display["A"] = 0
    i = 1
    while True:
        device_display["A"] = i
        program_output = execute_program(device_display)
        if program_output == device_display["program"]:
            break
        i += 1
    assert device_display["A"] == 117440


def solve():
    device_display = get_input("input")
    program_output = execute_program(device_display)
    print(program_output)


if __name__ == "__main__":
    test2()
