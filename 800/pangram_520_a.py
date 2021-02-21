class Pangram:

    pass


if __name__ == "__main__":
    n = int(input())
    nr_of_latin_characters = 26
    in_letters = set(input().lower())
    if len(in_letters) == nr_of_latin_characters:
        print('YES')
    else:
        print('NO')