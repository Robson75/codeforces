class DominoOnWindowsill:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        n, k1, k2 = list(map(int, input().split()))
        w, b = list(map(int, input().split()))
        possible_white = k1 // 2 + k2 // 2
        if k1 % 2 == 1 and k2 % 2 == 1:
            possible_white += 1
        possible_black = (n - k1) // 2 + (n - k2) // 2
        if (n - k1) % 2 == 1 and (n - k2) % 2 == 1:
            possible_black += 1
        if w <= possible_white and b <= possible_black:
            print('YES')
        else:
            print('NO')