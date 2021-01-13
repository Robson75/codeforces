class FairDivision:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        nr_of_pieces = int(input())
        weights = list(map(int, input().split()))
        if sum(weights) % 2 != 0:
            print("NO")
        elif weights.count(1) >= 2:
            print("YES")
        elif len(weights) % 2 == 0:
            print("YES")
        else:
            print("NO")
