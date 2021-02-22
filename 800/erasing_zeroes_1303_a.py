class ErasingZeroes:

    pass


if __name__ == "__main__":
    test_cases = int(input())
    for i in range(test_cases):
        s = input()
        possible_erase = 0
        erase = 0
        last_character = s[0]
        start_count = False
        for c in s[1:]:
            if last_character == '1' and c == '0':
                possible_erase += 1
                start_count = True
            elif last_character == '0' and c == '0' and start_count:
                possible_erase += 1
            elif c == '1' and start_count:
                start_count = False
                erase += possible_erase
                possible_erase = 0
            last_character = c
        print(erase)


