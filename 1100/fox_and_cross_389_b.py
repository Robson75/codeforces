class FoxAndCross:

    pass


def check_board(b):
    possible = 'YES'
    b_size = len(b)
    for i in range(board_size):
        for j in range(b_size):
            if b[i][j] == "#":
                if j == 0 or j == b_size - 1 or i > b_size - 3:
                    possible = 'NO'
                    return possible
                elif b[i+1][j-1] != "#" or b[i+1][j] != "#" or b[i+1][j+1] != "#" or b[i+2][j] != "#":
                    possible = 'NO'
                    return possible
                else:
                    b[i + 1][j - 1] = "used"
                    b[i + 1][j] = "used"
                    b[i + 1][j + 1] = "used"
                    b[i + 2][j] = "used"
    return possible


if __name__ == "__main__":
    board_size = int(input())
    board = []
    for n in range(board_size):
        line = list(input())
        board.append(line)
    print(check_board(board))

