class LittlePonyAndCrystalMine:

    pass


if __name__ == "__main__":
    n = int(input())
    stars = n - 1
    ds = 1
    for i in range(n):
        out_string = ''
        ds = n - 2 * abs(n // 2 - i)
        stars = 2 * abs(n // 2 - i)
        for s in range(stars // 2):
            out_string += '*'
        for d in range(ds):
            out_string += 'D'
        for s in range(stars // 2):
            out_string += '*'
        print(out_string)