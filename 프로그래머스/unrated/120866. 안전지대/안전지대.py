import numpy as np

def solution(board):
    board = np.array(board)
    rows, cols = np.where(board == 1)

    for r, c in zip(rows, cols):
        if r != 0 and c != 0:
            board[r - 1:r + 2, c - 1:c + 2] = 1
        elif r == 0 and c != 0:
            board[0:r + 2, c - 1:c + 2] = 1
        elif r != 0 and c == 0:
            board[r - 1:r + 2, 0:c + 2] = 1
        elif r == 0 and c == 0:
            board[0:r + 2, 0:c + 2] = 1
        else:
            board[r - 1:r + 2, c - 1:c + 2] = 1

    print(board)
    return len(board[board == 0])

