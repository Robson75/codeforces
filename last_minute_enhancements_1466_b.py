class LastMinuteEnhancements:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        nr_of_tones = int(input())
        tones = list(map(int, input().split()))
        distinct_tones = 1
        for i in range(nr_of_tones - 1):
            if tones[i + 1] <= tones[i]:
                tones[i + 1] = tones[i + 1] + 1
            if tones[i + 1] > tones[i]:
                distinct_tones += 1
        print(distinct_tones)