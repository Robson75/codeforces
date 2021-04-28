class ParkLighting:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        m, n = list(map(int, input().split()))
        if (m * n) % 2 == 0:
            print((m * n) // 2)
        else:
            print((m * n) // 2 + 1)
