def calculate_years(weight1, weight2):
    required_years = 0
    while weight1 <= weight2:
        required_years += 1
        weight1 *= 3
        weight2 *= 2

    return required_years


class BearAndBigBrother:
    pass


if __name__ == "__main__":
    test_nr_1 = 1
    test_nr_2 = 100
    # print(calculate_years(test_nr_1, test_nr_2))
    print(test_nr_2)
