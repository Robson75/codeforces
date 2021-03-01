class MagicalSticks:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        nr_of_sticks = int(input())
        if nr_of_sticks <= 2:
            print(1)
        else:
            print((nr_of_sticks + 1) // 2)
