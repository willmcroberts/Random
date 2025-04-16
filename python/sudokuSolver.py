SIZE = 9

def main():
    board = [
            [0,0,0,0,8,6,2,0,0],
            [0,2,4,0,0,0,0,0,0],
            [0,0,7,0,0,3,0,0,5],
            [0,0,0,5,7,0,0,0,6],
            [0,0,8,0,9,0,0,7,0],
            [0,4,0,0,0,0,0,0,0],
            [4,8,0,0,0,0,0,9,0],
            [1,9,0,4,5,0,0,0,3],
            [0,0,0,0,0,0,0,0,2]
        ]
    
    printBoard(board)
    
def printBoard(board):
    for i in board:
       print(i)
    
def isNumberInRow(board, number, row):
    for i in range(SIZE):
        if (board[row][i] == number):
            return True
    return False

def isNumberInColumn(board, number, column):
    for i in range(SIZE):
        if (board[i][column] == number):
            return True
    return False

def isNumberInBox(board, number, row, column):
    localBoxRow = row - row % 3
    localBoxColumn = column - column % 3

    for
main()
