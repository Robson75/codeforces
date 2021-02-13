class MinutesBeforeTheNewYear:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        h, m = map(int, input().split())
        print((24 - h) * 60 - m)
