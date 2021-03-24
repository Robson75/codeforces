class RemoveSmallest:
    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        a_sorted = sorted(a)
        current = a_sorted[0]
        possible = 'YES'
        for nr in a_sorted:
            if nr - current > 1:
                possible = 'NO'
            current = nr
        print(possible)
