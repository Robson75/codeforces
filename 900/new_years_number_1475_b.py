class NewYearsNumber:

    pass


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        nr_of_2020s = n // 2020
        extra = n % 2020
        if extra <= nr_of_2020s:
            print('YES')
        else:
            print('NO')
