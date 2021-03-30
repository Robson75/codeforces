class YetAnotherTwoIntegerProblem:


    pass


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        dif = abs(a - b)
        print((dif + 9) // 10)
