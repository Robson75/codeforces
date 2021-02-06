class WhiteSheet:

    pass


if __name__ == "__main__":
    white_coord = list(map(int, input().split()))
    black_1_coord = list(map(int, input().split()))
    black_2_coord = list(map(int, input().split()))
    x1 = white_coord[0]
    y1 = white_coord[1]
    x2 = white_coord[2]
    y2 = white_coord[3]
    x3 = black_1_coord[0]
    y3 = black_1_coord[1]
    x4 = black_1_coord[2]
    y4 = black_1_coord[3]
    x5 = black_2_coord[0]
    y5 = black_2_coord[1]
    x6 = black_2_coord[2]
    y6 = black_2_coord[3]
    can_be_seen = 'NO'

    # compare with the first black sheet and divide the white sheet into maximum 4 sub-sheets.
    # compare each of those with the other black sheet
    if x1 < x3:
        x7 = x1
        y7 = y1
        x8 = min(x2, x3)
        y8 = y2
        if x7 < x5 or y7 < y5 or x8 > x6 or y8 > y6:
            can_be_seen = 'YES'
    if x2 > x4:
        x9 = max(x1, x4)
        y9 = y1
        x10 = x2
        y10 = y2
        if x9 < x5 or y9 < y5 or x10 > x6 or y10 > y6:
            can_be_seen = 'YES'
    if y1 < y3:
        x11 = x1
        y11 = y1
        x12 = x2
        y12 = min(y2, y3)
        if x11 < x5 or y11 < y5 or x12 > x6 or y12 > y6:
            can_be_seen = 'YES'
    if y2 > y4:
        x13 = x1
        y13 = max(y1, y4)
        x14 = x2
        y14 = y2
        if x13 < x5 or y13 < y5 or x14 > x6 or y14 > y6:
            can_be_seen = 'YES'
    print(can_be_seen)