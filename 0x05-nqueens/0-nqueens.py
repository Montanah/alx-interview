#!/usr/bin/python3
"""N Queens"""

import sys


def printBoard(board):
    """Prints the board"""
    print("[", end="")
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end="")
                if i != len(board) - 1:
                    print(", ", end="")
    print("]")
    return


def isSafe(board, row, col):
    """Checks if a position is safe"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    """Solves the N Queen problem"""
    if col == len(board):
        printBoard(board)
        return True
    res = False
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0
    return res


def solveNQ(n):
    """Solves the N Queen problem"""
    board = [[0 for i in range(n)] for j in range(n)]
    if solveNQUtil(board, 0) is False:
        return False
    return True


if __name__ == "__main__":
    """Solves the N Queen problem"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solveNQ(n)
