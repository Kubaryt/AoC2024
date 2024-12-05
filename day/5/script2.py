from script1 import get_input, sort_pages_in_patterns, calculate_updates, validate_update


def correct_update(invalid_update: list[list[str]], pages_order) -> (list[list[str]], False):
    update_was_invalid = False
    print(invalid_update, "before")
    for i in range(len(invalid_update)):
        n = invalid_update[i]
        for num in invalid_update[i:]:
            if n == num:
                continue
            try:
                if num in pages_order[n]:
                    update_was_invalid = True
                    n_index = invalid_update.index(n)
                    del invalid_update[n_index]
                    invalid_update.insert(n_index + 1, n)
                    break
            except KeyError:
                continue
    if update_was_invalid:
        print(invalid_update, "after")
        return invalid_update
    else:
        print("no")
        return False


if __name__ == "__main__":
    patterns, updates = get_input("input")
    page_order = sort_pages_in_patterns(patterns)
    valid_updates = []
    for update in updates:
        if correct_update(update, page_order):
            while not validate_update(update, page_order):
                update = correct_update(update, page_order)
            valid_updates.append(update)
    print(calculate_updates(valid_updates))
