'''
Author: Prudhvik
Date: 24-08-2018
'''

def is_valid_game(game_grid):
    '''check's whether game isvalid'''
    x_count, o_count = 0, 0
    for each_row in game_grid:
        for each_box in each_row:
            if each_box == 'x':
                x_count += 1
            elif each_box == 'o':
                o_count += 1
            elif each_box == '.':
                pass
            else:
                return "invalid input"
    if abs(o_count - x_count) != 1:
        return "invalid game"

    return None

def horizontal_check(game_grid):
    '''checks for horizontal conditions'''
    for each_row in game_grid:
        if each_row.count(each_row[0]) == 3 and each_row[0] != '.':
            return each_row[0]
    return None

def vertical_check(game_grid):
    '''checks vertical'''
    win_count = 0
    win_flag = game_grid[0][0]
    grid_length = len(game_grid)
    for i in range(grid_length):
        if win_count == 3:
            break
        win_count = 0
        win_flag = game_grid[0][i]
        if win_flag == '.':
            continue
        for j in range(grid_length):
            if game_grid[j][i] == win_flag:
                win_count += 1
            else:
                break
    if win_count == 3:
        return win_flag
    return None

def diagonal_left_to_right(game_grid):
    '''checks diagonal left to right'''
    grid_length = len(game_grid)
    win_flag = game_grid[0][0]
    win_count = 0
    if win_flag != '.':
        for i in range(grid_length):
            if game_grid[i][i] == win_flag:
                win_count += 1
            else:
                break
    if win_count == 3:
        return win_flag
    return None

def diagonal_right_to_left(game_grid):
    '''checks diagonal right to left'''
    grid_length = len(game_grid)
    win_flag = game_grid[0][-1]
    win_count = 0
    if win_flag != '.':
        for i in range(grid_length):
            if game_grid[i][-i-1] == win_flag:
                win_count += 1
            else:
                break
    if win_count == 3:
        return win_flag
    return None

def play_game(game_grid):
    '''its playing game'''
    return is_valid_game(game_grid) or horizontal_check(game_grid) or \
    vertical_check(game_grid) or diagonal_left_to_right(game_grid) or \
    diagonal_right_to_left(game_grid) or "draw"


def main():
    GRID_LINES = 3
    INPUT_GRID = []
    for _ in range(GRID_LINES):
        INPUT_GRID.append(input().split())
    print(play_game(INPUT_GRID))

main()
