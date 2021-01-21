class FourSegments:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        line_lengths = list(map(int, input().split()))
        sorted_lengths = sorted(line_lengths)
        max_area = sorted_lengths[0] * sorted_lengths[2]
        print(max_area)