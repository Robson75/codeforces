class FavoriteSequence:
    pass


if __name__ == "__main__":
    test_cases = int(input())
    for t in range(test_cases):
        seq_length = int(input())
        seq = input().split()
        favorite = ''
        for i in range(seq_length // 2):
            favorite += seq[i]
            favorite += ' '
            favorite += seq[seq_length - 1 - i]
            favorite += ' '
        if seq_length % 2 != 0:
            favorite += seq[seq_length // 2]

        print(favorite)
