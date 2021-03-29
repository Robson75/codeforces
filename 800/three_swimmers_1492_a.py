class ThreeSwimmers:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        p, a, b, c = list(map(int, input().split()))
        if p % a == 0 or p % b == 0 or p % c == 0:
            print(0)
        else:
            time_a = a - (p - (p // a * a))
            time_b = b - (p - (p // b * b))
            time_c = c - (p - (p // c * c))
            wait_time = min(min(time_a, time_b), time_c)
            print(wait_time)