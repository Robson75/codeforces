class TwoRabbits:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        x, y, a, b = list(map(int, input().split()))
        if (y - x) % (a + b) != 0:
            print('-1')
        else:
            print((y - x) // (a + b))
