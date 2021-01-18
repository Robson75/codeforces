class CardsForFriends:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        in_parameters = list(map(int, input().split()))
        w = in_parameters[0]
        h = in_parameters[1]
        n = in_parameters[2]
        pieces = 1
        w_cuts = 0
        h_cuts = 0
        while w % 2 == 0:
            w_cuts += 1
            w = w // 2
        while h % 2 == 0:
            h_cuts += 1
            h = h // 2
        pieces = pieces * (2 ** (w_cuts + h_cuts))
        if pieces >= n:
            print("YES")
        else:
            print("NO")
