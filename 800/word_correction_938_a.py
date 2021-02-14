class WordCorrection:

    pass


if __name__ == "__main__":
    n = int(input())
    word = input()
    corrected_word = word[0]
    vowels = ['a', 'e' ,'i', 'o', 'u', 'y']
    for i in range(1, n):
        if word[i] not in vowels or word[i - 1] not in vowels:
            corrected_word += word[i]
    print(corrected_word)
