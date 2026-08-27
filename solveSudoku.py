def solveSudoku(board):

    ## checking every row, column and box
    def isValid(row, col):
        for y in range(9):
            # condition that checks if the cell is not itself
            if y == row:
                continue
            else:
                if board[y][col] == board[row][col]:
                    return False
        for x in range(9):
            # condition that checks if the cell is not itself
            if x == col:
                continue
            else:
                if board[row][x] == board[row][col]:
                    return False
        ## coords for finding the beginning of a certain box
        box_row = (row//3) * 3
        box_col = (col//3) * 3

        # looping from the beginning to the end of the box
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if j == col and i == row:
                    continue
                else:
                    if board[i][j] == board[row][col]:
                        return False
        return True

    
    def backtrack(board, row, col):
        # if row == 9 means that the board is solved
        if row == 9:
            return True
        # time to go to the next row
        elif col == 9:
            return backtrack(board, row+1, 0)
        # if the current cell is prefilled skips it
        elif board[row][col] != ".":
            return backtrack(board, row, col+1)
        else:
            for i in range(1,10):
                board[row][col] = str(i)
                ## now the heart of the function: it fills in every possible digit,
                ## decides whats right by filling every other cell in the board (col+1).
                ## if it fails it BACKTRACKS and checks another digit  
                if isValid(row, col):
                    ## the heart
                    if backtrack(board, row, col+1):
                        return True
                    board[row][col] = "."
                else:
                    continue


            board[row][col] = "."
            return False

    
    backtrack(board, 0, 0)
    return board




board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(solveSudoku(board))


# set_rows = []
# set_cols = []
# set_boxes = []


