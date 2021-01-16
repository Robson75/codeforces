class TernarySequence:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        values_a = list(map(int, input().split()))
        values_b = list(map(int, input().split()))
        plus_2s = min(values_a[2], values_b[1])
        if values_a[2] > values_b[1]:
            extra_2s = values_a[2] - values_b[1]
        else:
            extra_2s = 0

        minus_2s = max(0, values_b[2] - values_a[0] - extra_2s)

        max_sum = 2 * (plus_2s - minus_2s)
        print(max_sum)
