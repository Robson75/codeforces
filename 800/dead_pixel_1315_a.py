class DeadPixel:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        a, b, x, y = list(map(int, input().split()))
        max_width = max(x, a - x - 1)
        max_height = max(y, b - y - 1)
        print(max(b * max_width, a * max_height))