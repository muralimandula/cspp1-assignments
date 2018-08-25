'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    # horizontal
    for i in range(9):
        horizontal_rows = sudoku[i]
        if "".join(sorted(horizontal_rows)) != "123456789":
            return False

    # vertical columns
    for i in range(9):
        vertical_coliumns = []
        for j in range(9):
            vertical_coliumns.append(sudoku[j][i])
        if "".join(sorted(vertical_coliumns)) != "123456789":
            return False

    # for first Horizontal 3*3 grid
    if "".join(sorted(sudoku[0][0]+sudoku[0][1]+sudoku[0][2]+ sudoku[1][0]+ sudoku[1][1]\
        +sudoku[1][2]+sudoku[2][0]+sudoku[2][1]+sudoku[2][2])) != "123456789":
        return False
    if "".join(sorted(sudoku[0][3]+sudoku[0][4]+sudoku[0][5]+ sudoku[1][3]+ sudoku[1][4]\
        +sudoku[1][5]+sudoku[2][3]+sudoku[2][4]+sudoku[2][5])) != "123456789":
        return False
    if "".join(sorted(sudoku[0][6]+sudoku[0][7]+sudoku[0][8]+ sudoku[1][6]+ sudoku[1][7]\
        +sudoku[1][8]+sudoku[2][6]+sudoku[2][7]+sudoku[2][8])) != "123456789":
        return False


    # below for second horizontal 3*3 column
    if "".join(sorted(sudoku[3][0]+sudoku[3][1]+sudoku[3][2]+ sudoku[4][0]+ sudoku[4][1]\
        +sudoku[4][2]+sudoku[5][0]+sudoku[5][1]+sudoku[5][2])) != "123456789":
        return False
    if "".join(sorted(sudoku[3][3]+sudoku[3][4]+sudoku[3][5]+ sudoku[4][3]+ sudoku[4][4]\
        +sudoku[4][5]+sudoku[5][3]+sudoku[5][4]+sudoku[5][5])) != "123456789":
        return False
    if "".join(sorted(sudoku[3][6]+sudoku[3][7]+sudoku[3][8]+ sudoku[4][6]+ sudoku[4][7]\
        +sudoku[4][8]+sudoku[5][6]+sudoku[5][7]+sudoku[5][8])) != "123456789":
        return False

    # below for third horizontal 3*3 column
    if "".join(sorted(sudoku[3][0]+sudoku[3][1]+sudoku[3][2]+ sudoku[4][0]+ sudoku[4][1]\
        +sudoku[4][2]+sudoku[5][0]+sudoku[5][1]+sudoku[5][2])) != "123456789":
        return False
    if "".join(sorted(sudoku[3][3]+sudoku[3][4]+sudoku[3][5]+ sudoku[4][3]+ sudoku[4][4]\
        +sudoku[4][5]+sudoku[5][3]+sudoku[5][4]+sudoku[5][5])) != "123456789":
        return False
    if "".join(sorted(sudoku[3][6]+sudoku[3][7]+sudoku[3][8]+ sudoku[4][6]+ sudoku[4][7]\
        +sudoku[4][8]+sudoku[5][6]+sudoku[5][7]+sudoku[5][8])) != "123456789":
        return False


    return True


def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''

    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for _ in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
