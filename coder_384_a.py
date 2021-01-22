class Coder:

    pass


if __name__ == "__main__":
    side_squares = int(input())
    squares = side_squares * side_squares
    if squares % 2 == 0:
        coders = squares // 2
    else:
        coders = squares // 2 + 1
    print(coders)
    for line in range(side_squares):
        line_config = ""
        for square in range(side_squares):
            if line % 2 == 0:
                if square % 2 == 0:
                    line_config += "C"
                else:
                    line_config += "."
            else:
                if square % 2 == 0:
                    line_config += "."
                else:
                    line_config += "C"
        print(line_config)
