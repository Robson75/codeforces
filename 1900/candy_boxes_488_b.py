class CandyBoxes:
    pass


if __name__ == "__main__":
    boxes = int(input())
    candy_supply = []
    for i in range(boxes):
        candies = int(input())
        candy_supply.append(candies)
    candy_supply = sorted(candy_supply)
    if boxes == 4:
        c_range = candy_supply[3] - candy_supply[0]
        a_mean = (candy_supply[0] + candy_supply[1] + candy_supply[2] + candy_supply[3]) / 4
        median = (candy_supply[2] + candy_supply[1]) / 2
        if c_range == a_mean == median:
            print('YES')
        else:
            print('NO')
    elif boxes == 0:
        print('YES')
        candy_supply = [1, 2, 2, 3]
        for box in candy_supply:
            print(box)
    elif boxes == 1:
        print('YES')
        x1 = candy_supply[0]
        candy_supply.append(2 * x1)
        candy_supply.append(2 * x1)
        candy_supply.append(3 * x1)
        print(candy_supply[1])
        print(candy_supply[2])
        print(candy_supply[3])
    elif boxes == 3:
        # box 1, 2, 3
        median = (candy_supply[1] + candy_supply[2]) / 2
        if 2 * candy_supply[0] == median:
            print('YES')
            candy_supply.append(int(median * 3 / 2))
            print(candy_supply[3])
        # box 1, 2, 4 or 1, 3, 4
        elif candy_supply[2] == candy_supply[0] * 3:
            print('YES')
            x1 = candy_supply[0]
            x4 = candy_supply[2]
            x2 = candy_supply[1]
            x3 = 4 * x1 - x2
            print(int(x3))
            if x3 > x2:
                temp = x2
                x2 = x3
                x3 = temp
            candy_supply = [x1, x2, x3, x4]

        # box 2, 3, 4
        elif 4 * candy_supply[2] == 3 * (candy_supply[0] + candy_supply[1]) and candy_supply[2] % 3 == 0:
            print('YES')
            x4 = candy_supply[2]
            x2 = candy_supply[0]
            x3 = candy_supply[1]
            x1 = x4 / 3
            candy_supply = [x1, x2, x3, x4]
            print(int(x1))
        else:
            print('NO')
    elif boxes == 2:
        # box 1, 2
        x1 = candy_supply[0]
        x2 = candy_supply[1]
        if 2 * x1 >= x2:
            print('YES')
            x3 = 4 * x1 - x2
            x4 = 3 * x1
            candy_supply.append(x3)
            candy_supply.append(x4)
            print(int(x3))
            print(int(x4))
        # box 1, 3 (and 1, 4)
        elif 3 * candy_supply[0] >= candy_supply[1] >= 2 * candy_supply[0]:
            x1 = candy_supply[0]
            x3 = candy_supply[1]
            x2 = 4 * x1 - x3
            x4 = 3 * x1
            candy_supply = [x1, x2, x3, x4]
            print('YES')
            print(int(x2))
            print(int(x4))
        # box 2, 3
        elif (candy_supply[0] > 0 and (candy_supply[0] + candy_supply[1]) % 4 == 0 and
              (candy_supply[0] + candy_supply[1]) / 2 >= candy_supply[1] - candy_supply[0]):
            x2 = candy_supply[0]
            x3 = candy_supply[1]
            x1 = (candy_supply[0] + candy_supply[1]) / 4
            x4 = 3 * x1
            candy_supply = [x1, x2, x3, x4]
            print('YES')
            print(int(x1))
            print(int(x4))
        # box 2, 4
        elif candy_supply[0] * 3 / 2 <= candy_supply[1] <= 3 * candy_supply[0] and candy_supply[1] % 3 == 0:
            x2 = candy_supply[0]
            x4 = candy_supply[1]
            x1 = x4 / 3
            x3 = 4 / 3 * x4 - x2
            candy_supply = [x1, x2, x3, x4]
            print('YES')
            print(int(x1))
            print(int(x3))
        # box 3, 4
        elif (candy_supply[0] + 1) * 3 / 4 <= candy_supply[1] <= candy_supply[0] * 3 / 2 and candy_supply[1] % 3 == 0:
            x2 = candy_supply[0]
            x4 = candy_supply[1]
            x1 = x4 / 3
            x3 = 4 / 3 * x4 - x2
            candy_supply = [x1, x2, x3, x4]
            print('YES')
            print(int(x1))
            print(int(x3))
        else:
            print('NO')
