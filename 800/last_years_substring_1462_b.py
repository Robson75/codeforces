class LastYearsSubstring:
    pass


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        n = int(input())
        digits = input()
        found = False
        if (digits[0] == '2' and digits[n - 3::] == '020' or
                digits[:2] == '20' and digits[n - 2:] == '20' or
                digits[:3] == '202' and digits[n - 1:] == '0' or
                digits[:4] == '2020' or
                digits[n - 4:] == '2020'):
            print('YES')
        else:
            print('NO')
