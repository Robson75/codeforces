class Rewards:

    pass


if __name__ == "__main__":
    cups = sum(list(map(int, input().split())))
    medals = sum(list(map(int, input().split())))
    shelves = int(input())
    shelves_for_cups = cups // 5
    if cups % 5 != 0:
        shelves_for_cups += 1
    shelves_for_medals = medals // 10
    if medals % 10 != 0:
        shelves_for_medals += 1
    if shelves_for_medals + shelves_for_cups > shelves:
        print('NO')
    else:
        print('YES')

