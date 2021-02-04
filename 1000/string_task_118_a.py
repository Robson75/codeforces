class StringTask:

    pass


if __name__ == "__main__":
    in_string = input()
    in_string = in_string.lower()
    vowels = ['a', 'o', 'u', 'y', 'e', 'i']
    out_string = ''
    for c in in_string:
        if c not in vowels:
            out_string += '.'
            out_string += c
    print(out_string)
