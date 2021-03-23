class PrisonBreak:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        a, b = list(map(int, input().split()))
        print(a * b)
