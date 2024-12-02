from script1 import get_input, MethodOfChange


def validate_report(report: list[str], starting_value: int, max_bad_values: int = 1) -> bool:
    last_number = int(report[0])
    if last_number > int(report[starting_value]):
        method_of_change = MethodOfChange.DECREASING
    elif last_number < int(report[starting_value]):
        method_of_change = MethodOfChange.INCREASING
    else:
        return False

    bad_values = 0
    for number in report[starting_value:]:
        number = int(number)
        difference = abs(number - last_number)
        if difference > 3 or difference < 1:
            bad_values += 1
            continue

        match method_of_change:
            case MethodOfChange.INCREASING:
                if number < last_number:
                    bad_values += 1
                    continue
            case MethodOfChange.DECREASING:
                if number > last_number:
                    bad_values += 1
                    continue
        last_number = number
    if bad_values > max_bad_values:
        return False
    else:
        return True


def calculate_valid_reports(reports_list: list[list[str]]) -> int:
    valid_reports = 0
    for report in reports_list:
        if validate_report(report, 1):
            valid_reports += 1
            continue
        if validate_report(report[1:], 1, 0):
            valid_reports += 1
            continue
        if validate_report(report, 2, 0):
            valid_reports += 1
            continue
    return valid_reports

if __name__ == "__main__":
    reports = get_input("input")
    print(calculate_valid_reports(reports))
