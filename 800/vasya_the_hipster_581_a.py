class VasyaTheHipster:

    pass


if __name__ == "__main__":
    red, blue = list(map(int, input().split()))
    days_different = min(red, blue)
    socks_same = max(red, blue) - days_different
    days_same = socks_same // 2
    print(str(days_different) + ' ' + str(days_same))
