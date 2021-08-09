board = [
    [0, 1, 0, 0, 6, 0, 0, 7, 2],
    [0, 5, 0, 0, 9, 0, 0, 0, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 8, 0, 1, 9, 0, 0, 0],
    [0, 0, 2, 0, 0, 4, 5, 0, 0],
    [4, 0, 0, 6, 8, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [8, 0, 0, 4, 0, 0, 0, 6, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0]
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 or j == 0:
                print('| ', end='')

            if j == 8:
                print(str(board[i][j]) + ' | ')

            else:
                print(str(board[i][j]) + ' ', end='')


def check_validity(board, num, pos):
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def check_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def solve(board):

    find = check_empty(board)

    if find is None:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if check_validity(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

print("Here is the unsolved board:")
print_board(board)
solve(board)
print()
print("Here is the solved board:")
print_board(board)
