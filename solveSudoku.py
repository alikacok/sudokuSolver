def solveSudoku(board):
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]

    for i in range(9):
        # generating a set from what we have in a row
        set1 = set(board[i])
        if "." in set1:
            set1.remove(".")
        row_sets[i] = set1
        arr = []

        for j in range(9):
            # same sht here, but iterating through rows to get the whole col
            arr.append(board[j][i])
            set2 = set(arr)
            if "." in set2:
                set2.remove(".")
            col_sets[i] =set2 


    box_sets = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            box_row = (i//3)
            box_col = (j//3)
            # box coords
            box = box_row * 3 + box_col
            if board[i][j] == ".":
                continue
            else:
                box_sets[box].add(board[i][j])


    def isValid(row, col):
        cell = board[row][col]
        # checking repetitions in the rows and cols
        if (cell in row_sets[row]) or (cell in col_sets[col]):
            return False
        br = row//3
        bc = col//3
        # box coords again
        box_index = br * 3 + bc
        # checking the 3*3 box
        if cell in box_sets[box_index]:
            return False
 
        return True

    # heart of the solver
    def backtrack(board, row, col):
        # if the rows are done, then we finished the board
        if row == 9:
            return True
        # going to next row
        elif col == 9:
            return backtrack(board, row+1, 0)
        # if there's a number skipping the cell
        elif board[row][col] != ".":
            return backtrack(board, row, col+1)
        else:
            for i in range(1,10):
                br = row//3
                bc = col//3
                box_index = br * 3 + bc
                board[row][col] = str(i)
                # if it goes thru the check, it adds it to the row, col and box sets
                if isValid(row, col):
                    row_sets[row].add(board[row][col])
                    col_sets[col].add(board[row][col])
                    box_sets[box_index].add(board[row][col])
                    # it BACKTRACKS till the end of the board to check if the current digit is ok
                    if backtrack(board, row, col+1):
                        return True
                    # if not, it js removes it from everywhere
                    row_sets[row].remove(board[row][col])
                    col_sets[col].remove(board[row][col])
                    box_sets[box_index].remove(board[row][col])
                    board[row][col] = "."

            # resets it back "." if nothing has worked out
            board[row][col] = "."
            return False
    backtrack(board, 0, 0)
    return board

