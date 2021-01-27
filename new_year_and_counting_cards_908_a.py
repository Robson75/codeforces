class NewYearAndCountingCards:

    pass


if __name__ == "__main__":
    cards = input()
    vowels = ['a', 'e', 'i', 'o', 'u']
    odd = ['1', '3', '5', '7', '9']
    flips = sum([1 for c in cards if (c in vowels or c in odd)])
    print(flips)
