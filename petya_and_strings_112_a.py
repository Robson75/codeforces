class PetyaAndStrings:
    pass


if __name__ == "__main__":
    string1 = input().lower()
    string2 = input().lower()
    if string1 > string2:
        result = 1
    elif string1 < string2:
        result = -1
    else:
        result = 0

    print(result)
