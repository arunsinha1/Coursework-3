
import copy

def random_grid(grid):
    # This will start the Sudoku grid with lists of random possible values for each block.
    unfilled_block = [1,2,3,4,5,6,7,8,9]
    for row in range(9):
        for column in range(9):
            if grid[row][column] == 0:
                grid[row][column] = copy.deepcopy(unfilled_block)
    print(grid)

def possibility_removal(grid,row,column,value):
     # Automatically removes the possible values from the block's column and row.
    row_ = [block for block in grid[row] if type(block) == list]
    column_ =[grid[i][column] for i in range(9) if type(grid[i][column]) == list]
    for block in row_:
        if value in block:
            block.remove(value)
    for block in column_:
        if value in block:
            block.remove(value)
            
    row_1, column_1 = 3* (row // 3), 3 * (column // 3)
    for i in range(row_1, row_1 + 3):
         #It loops through all the blocks in the 3x3 area, checks to see if list of possible values is among them and removes them if it is.
        for j in range(column_1, column_1 + 3):
            if type(grid[i][j]) == list:
                if value in grid[i][j]:
                    grid[i][j].remove(value)

def value_finder(grid):
     # Finds blocks with values and inserts them in the block.
     progress = False
     for row in range(9):
         for column in range(9):
             block = grid[row][column]
             if type(block) == list and len(block) == 1:
                 value = block[0]
                 grid[row][column] = value
                 possibility_removal(grid, row, column, value)
                 progress = True
     return progress

def min_value(grid):
    # This will choose the block with the minimum number of possible values.
    min_possibility = None
    min_ = 10
    for row in range(9):
        for column in range(9):
            if type(grid[row][column]) == list and len(grid[row][column]) < min_:
                min_possibility = grid[row][column]
                min_ = len(min_possibility)
                min_row, min_col = row, column
    return min_row, min_col, min_possibility

def is_valid(grid, row, column, num):
    # A loop is used by the function to determine whether the number occurs in the same row and column as the given indices. If it exists, the function returns False immediately, indicating that the number is invalid. 
    for i in range(9):
        if grid[row][i] == num:
            return False
        if grid[i][column] == num:
            return False 
    row_, column_ = 3 * (row // 3 ), 3 * (column // 3)
    for i in range(row_, row_ + 3):
        for j in range(column_, column_ + 3):
            if grid[i][j] == num:
                return False
    return True 
    
def empty_block(grid):
    # checks if the block in the grid is 0 which will indicate an empty block.
    for row in range(9):
        for column in range(9):
             if grid[row][column] == 0:
                 return row, column
    return None, None
 
def solve(grid):
    # The solution() function identifies the first empty block in the grid and returns True if there are no more empty blocks left, indicating that the problem has been solved. Then it iterates through numbers 1-9, calling the is_valid() function to see if each number is valid to be placed in the empty block. If a number is valid, it is entered into the block, and solution() is called again. The puzzle has been solved if the recursive call returns True, and the function returns True. If it does not, the block is reset to 0, and the function continues to attempt different integers. If all possible integers are attempted but none of them work, the method returns False.
    
    row, column = empty_block(grid)
    if row is None and column is None:
        return True
 
    for num in range(1, 10):
        if is_valid(grid, row, column, num):
             grid[row][column] = num
             if solve(grid):
                 return True
             grid[row][column] = 0
 
    return False
 
Grid_Fig_1 = [
     [5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 8, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]
 ]
 
solve(Grid_Fig_1)
for row in Grid_Fig_1:
    for block in row:
        print(block, end= " ")
