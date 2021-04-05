class AntiKnapsack:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        n, k = list(map(int, input().split()))
        numbers = []
        for nr in range(n + 1):
            if nr >= k / 2 and nr != k:
                numbers.append(nr)
        print(len(numbers))
        print(*numbers)
