class FoxAndSnake:

    pass


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    for row in range(n):
        if (row + 1) % 2 != 0:
            pattern = '#' * m
        elif (row + 1) % 4 == 0:
            pattern = '#' + '.' * (m - 1)
        else:
            pattern = '.' * (m - 1) + '#'
        print(pattern)
