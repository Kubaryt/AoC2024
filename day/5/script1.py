import math


def get_input(file_name: str) -> (list[list[str, str]], list[list[str]]):
    with open(file_name, "r") as file:
        patterns = list()
        updates = list()
        for line in file:
            if line.find("|") != -1:
                line = line.strip().split("|")
                patterns.append(line)
            elif line.strip() != '':
                line = line.strip().split(",")
                updates.append(line)

    return patterns, updates


def sort_pages_in_patterns(pattern_list: list[list[str, str]]) -> dict:
    pages_order = dict()
    for pattern in pattern_list:
        if pattern[1] in pages_order.keys():
            pages_order[pattern[1]].append(pattern[0])
        else:
            pages_order.update({pattern[1]: [pattern[0]]})
    print(pages_order)
    return pages_order


def validate_update(_update: list[str], pages_order: dict) -> bool:
    update_valid = True
    for i in range(len(_update)):
        n = _update[i]
        for num in _update[i:]:
            if n == num:
                continue
            try:
                if num in pages_order[n]:
                    update_valid = False
                    break
            except KeyError:
                continue
        if not update_valid:
            break

    return update_valid


def calculate_updates(updates_list: list[list[str]]) -> int:
    total = 0
    for update in updates_list:
        print(update)
        middle = int(update[math.ceil((len(update) - 1) / 2)])
        total += middle
    return total


if __name__ == "__main__":
    patterns, updates = get_input("input")
    page_order = sort_pages_in_patterns(patterns)
    valid_updates = []
    for update in updates:
        if validate_update(update, page_order):
            valid_updates.append(update)
    print(calculate_updates(valid_updates))