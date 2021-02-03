class JapaneseCrosswordsStrikeBack:

    pass


if __name__ == "__main__":
    (n, x) = map(int, input().split())
    encoding = list(map(int, input().split()))
    zeros = n - 1
    ones = sum(encoding)
    if zeros + ones == x:
        print('YES')
    else:
        print('NO')
