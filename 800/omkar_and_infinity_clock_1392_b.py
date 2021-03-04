class OmkarAndInfinityClock:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n, k = map(int, input().split())
        numbers = list(map(int, input().split()))
        max_number = max(numbers)
        new_numbers = [max_number - nr for nr in numbers]
        max_number_2 = max(new_numbers)
        new_numbers_2 = [max_number_2 - nr for nr in new_numbers]
        if k == 1:
            print(*new_numbers)
        elif k % 2 == 0:
            print(*new_numbers_2)
        else:
            print(*new_numbers)


