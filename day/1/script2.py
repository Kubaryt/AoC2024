from script1 import get_input


def calculate_similarities(list_of_rows: list[list[int]]) -> dict[str, int]:
    row_1 = list_of_rows[0]
    row_2 = list_of_rows[1]
    similarities = dict()
    for n1 in row_1:
        similiarity = 0
        for n2 in row_2:
            if n1 == n2:
                similiarity += 1
        similiarity *= n1
        if not str(n1) in similarities:
            similarities.update({f"{n1}": similiarity})
        else:
            similarities[str(n1)] += similiarity
    return similarities


def sum_similarities(dict_of_similiarities: dict[str, int]) -> int:
    total = 0
    for value in dict_of_similiarities.values():
        total += value
    return total


if __name__ == "__main__":
    all_rows = get_input("input")
    rows_similarities = calculate_similarities(all_rows)
    print(sum_similarities(rows_similarities))
