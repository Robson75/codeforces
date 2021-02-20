class DivisibilityProblem:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        a, b = list(map(int, input().split()))
        dif = b - a
        if dif > 0:
            print(dif)
        elif a % b == 0:
            print(0)
        else:
            print(((a // b + 1) * b) - a)


