class TextVolume:

    pass


if __name__ == "__main__":
    text_length = int(input())
    words = list(input().split())
    max_volume = 0
    for word in words:
        max_volume = max(max_volume, sum([1 for letter in word if str(letter).isupper()]))
    print(max_volume)
