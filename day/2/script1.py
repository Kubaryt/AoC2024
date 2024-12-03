from enum import Enum, auto


class MethodOfChange(Enum):
    INCREASING = auto()
    DECREASING = auto()
    NONE = auto()


def get_input(file_name: str) -> list[list[str]]:
    with open(file_name, "r") as f:
        all_lines = []
        for line in f:
            line = line.strip().split(" ")
            all_lines.append(line)
        return all_lines


def validate_reports(reports_list: list[list[str]]) -> int:
    valid_reports = 0
    for report in reports_list:
        # decreasing or increasing
        method_of_change = MethodOfChange.NONE
        last_number = ""
        report_valid = 1
        for number in report:
            number = int(number)
            if last_number == "":
                last_number = number
                continue
            if method_of_change == MethodOfChange.NONE:
                if last_number > number:
                    method_of_change = MethodOfChange.DECREASING
                elif last_number < number:
                    method_of_change = MethodOfChange.INCREASING
                else:
                    report_valid = 0
                    break
            match method_of_change:
                case MethodOfChange.DECREASING:
                    if last_number <= number:
                        report_valid = 0
                        break
                    if abs(number - last_number) not in [1, 2, 3]:
                        report_valid = 0
                        break
                case MethodOfChange.INCREASING:
                    if last_number >= number:
                        report_valid = 0
                        break
                    if abs(last_number - number) not in [1, 2, 3]:
                        report_valid = 0
                        break
            last_number = number

        if report_valid:
            valid_reports += 1

    return valid_reports


if __name__ == "__main__":
    reports = get_input("input")
    print(validate_reports(reports))
