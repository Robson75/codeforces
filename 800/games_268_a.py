class Games:

    pass


if __name__ == "__main__":
    n = int(input())
    home = []
    guest = []
    change = 0
    for i in range(n):
        h, a = map(int, input().split())
        home.append(h)
        guest.append(a)
    for color1 in home:
        for color2 in guest:
            if color1 == color2:
                change += 1
    print(change)