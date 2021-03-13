class NewYearAndHurry:

    pass


def arithmetic_sum(q):
    q1 = 5
    diff = 5
    qn = q1 + (q - 1) * diff
    return q * (q1 + qn) / 2


if __name__ == "__main__":
    n, k = list(map(int, input().split()))

    # 4 hours competition, k minutes left needed
    available_time = 4 * 60 - k

    questions_answered = n
    elapsed_time = arithmetic_sum(questions_answered)
    if elapsed_time > available_time:
        low = 0
        high = n
        while high > low:
            questions_answered = low + (high - low) // 2
            elapsed_time = arithmetic_sum(questions_answered)
            if elapsed_time > available_time:
                high = min((high - 1), high - (high - low) // 2)
            else:
                low = max((low + 1), low + (high - low) // 2)
    print(questions_answered)


