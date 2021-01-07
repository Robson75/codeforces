class BeautifulMatrix:
    pass


if __name__ == "__main__":
    rows = 5
    middle = 3
    row_shift = 0
    col_shift = 0
    row = 0
    for i in range(rows):
        row_data = input().split()
        if '1' in row_data:
            row_shift = abs(middle - (i + 1))
            col_shift = abs(middle - (row_data.index('1') + 1))
    print(row_shift + col_shift)
