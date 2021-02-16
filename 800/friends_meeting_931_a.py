class FriendsMeeting:

    pass


if __name__ == "__main__":
    a = int(input())
    b = int(input())
    diff = abs(a - b)
    half_diff = diff // 2
    if half_diff % 2 == 0:
        tiredness = 2 * (half_diff + 1) * (half_diff // 2)
    else:
        tiredness = 2 * (half_diff + 1) * (half_diff // 2) + 2 * (half_diff // 2 + 1)
    if diff % 2 != 0:
        tiredness += half_diff + 1
    print(tiredness)

