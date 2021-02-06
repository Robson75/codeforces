class Presents:

    pass


if __name__ == "__main__":
    friends = int(input())
    gift_order = list(map(int, input().split()))
    receiver_giver = [None] * friends
    for index, friend in enumerate(gift_order):
        receiver_giver[friend - 1] = index + 1
    print(*receiver_giver)