import random
import copy
import time
#Grids 1-5 are 2x2
grid1 = [
        [1, 0, 4, 2],
        [4, 2, 1, 3],
        [2, 1, 3, 4],
        [3, 4, 2, 1]]
grid2 = [
        [1, 0, 4, 2],
        [4, 2, 1, 3],
        [2, 1, 0, 4],
        [3, 4, 2, 1]]
grid3 = [
        [1, 0, 4, 2],
        [4, 2, 1, 0],
        [2, 1, 0, 4],
        [0, 4, 2, 1]]
grid4 = [
        [1, 0, 4, 2],
        [0, 2, 1, 0],
        [2, 1, 0, 4],
        [0, 4, 2, 1]]
grid5 = [
        [1, 0, 0, 2],
        [0, 0, 1, 0],
        [0, 1, 0, 4],
        [0, 0, 0, 1]]
#easy1
#grid 6-7 is 3x3
grid6 = [
        [9, 0, 6, 0, 0, 1, 0, 4, 0],
        [7, 0, 1, 2, 9, 0, 0, 6, 0],
        [4, 0, 2, 8, 0, 6, 3, 0, 0],
        [0, 0, 0, 0, 2, 0, 9, 8, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 9, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 3, 7, 0, 8, 4, 0, 9],
        [0, 4, 0, 0, 1, 3, 7, 0, 6],
        [0, 6, 0, 9, 0, 0, 1, 0, 8]]
# easy2
grid7 = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]]
#easy3   
#grid8 is 2x3
grid8 = [
        [0, 3, 0, 4, 0, 0],
        [0, 0, 5, 6, 0, 3],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 3, 0, 5],
        [0, 6, 4, 0, 3, 1],
        [0, 0, 1, 0, 4, 6]]
#med1
# grid 9-11 is 3x3
grid9 = [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 1],
        [3, 6, 9, 0, 8, 0, 4, 0, 0],
        [0, 0, 0, 0, 0, 6, 8, 0, 0],
        [0, 0, 0, 1, 3, 0, 0, 0, 9],
        [4, 0, 5, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 3, 0, 0],
        [0, 0, 6, 0, 0, 7, 0, 0, 0],
        [1, 0, 0, 3, 4, 0, 0, 0, 0]]

# med2
grid10 =[
        [8, 0, 9, 0, 2, 0, 3, 0, 0],
        [0, 3, 7, 0, 6, 0, 5, 0, 0],
        [0, 0, 0, 4, 0, 9, 7, 0, 0],
        [0, 0, 2, 9, 0, 1, 0, 6, 0],
        [1, 0, 0, 3, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 3],
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [5, 0, 0, 0, 0, 0, 0, 1, 4],
        [0, 0, 0, 2, 8, 4, 6, 0, 5]]
#hard1
grid11 =[
        [0, 2, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 6, 0, 4, 0, 0, 0, 0],
        [5, 8, 0, 0, 9, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 3, 0, 0, 4],
        [4, 1, 0, 0, 8, 0, 6, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 5],
        [2, 0, 0, 0, 1, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 1, 0, 0, 8, 0, 5, 7]]
grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2), (grid6, 3, 3), (grid7, 3, 3), (grid8, 2, 3), (grid9, 3, 3), (grid10, 3, 3), (grid11, 3, 3)]

'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

def check_section(section, n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]):
        return True
    return False

def get_squares(grid, n_rows, n_cols):
    squares = []
    for i in range(n_cols):
        rows = (i*n_rows, (i+1)*n_rows)
        for j in range(n_rows):
            cols = (j*n_cols, (j+1)*n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square +=line
            squares.append(square)
    return(squares)

def check_solution(grid, n_rows, n_cols):
    '''
    This function is used to check whether a sudoku board has been correctly solved
    args: grid - representation of a suduko board as a nested list.
    returns: True (correct solution) or False (incorrect solution)
    '''
    n = n_rows*n_cols
    for row in grid:
        if check_section(row, n) == False:
            return False
    for i in range(n_rows**2):
        column = []
        for row in grid:
            column.append(row[i])
        if check_section(column, n) == False:
            return False
    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) == False:
            return False
    return True

def find_empty(grid):
    '''
    This function returns the index (i, j) to the first zero element in a sudoku grid
    If no such element is found, it returns None

    args: grid
    return: A tuple (i,j) where i and j are both integers, or None
    '''
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                return (i, j)
    return None

def recursive_solve(grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found
    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''
    #n is the maximum integer considered in this board
    n = n_rows*n_cols
    #initialise a set which stores the possible numbers which can go in the empty space
    numbers=set(list(range(1, n+1)))
    #Find an empty place in the grid
    empty = find_empty(grid)
    #If there's no empty places left, check if we've found a solution
    if not empty:
    #If the solution is correct, return it.
        if check_solution(grid, n_rows, n_cols):
            return grid 
        else:
            #If the solution is incorrect, return None
            return None
    #remove the values which are already found in the rows and coloumns of the empty space
    numbers = numbers - set(grid[empty[0]])
    numbers = numbers - set(grid[i][empty[1]] for i in range(len(grid)))
    square_row, square_col = empty[0] // n_rows, empty[1] // n_cols
    for i in range(square_row * n_rows, (square_row + 1) * n_rows):
        for j in range(square_col * n_cols, (square_col + 1) * n_cols):
            numbers.discard(grid[i][j])
    for i in numbers:           
            #Place the value into the empty space in the grid
            grid[empty[0]][empty[1]] = i
            #Recursively solve the grid
            ans = recursive_solve(grid, n_rows, n_cols)
            #If we've found a solution, return it
            if ans:
                return ans 
            #If we couldn't find a solution, that must mean this value is incorrect.
            #Reset the grid for the next iteration of the loop
            grid[empty[0]][empty[1]] = 0 
    #If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None

def random_solve(grid, n_rows, n_cols, max_tries=50000):
    '''
    This function uses random trial and error to solve a Sudoku grid
    args: grid, n_rows, n_cols, max_tries
    return: A solved grid (as a nested list), or the original grid if no solution is found
    '''
    for i in range(max_tries):
        possible_solution = fill_board_randomly(grid, n_rows, n_cols)
        if check_solution(possible_solution, n_rows, n_cols):
            return possible_solution
    return grid

def fill_board_randomly(grid, n_rows, n_cols):
    '''
    This function will fill an unsolved Sudoku grid with random numbers
    args: grid, n_rows, n_cols
    return: A grid with all empty values filled in
    '''
    n = n_rows*n_cols
    #Make a copy of the original grid
    filled_grid = copy.deepcopy(grid)
    #Loop through the rows
    for i in range(len(grid)):
        #Loop through the columns
        for j in range(len(grid[0])):
            #If we find a zero, fill it in with a random integer
            if grid[i][j] == 0:
                filled_grid[i][j] = random.randint(1, n)
    return filled_grid

def solve(grid, n_rows, n_cols):
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''    
    # return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)

'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''
def main():
    points = 0
    print("Running test script for coursework 1")
    print("====================================")
    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i+1))
        start_time = time.time()
        solution = solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        print(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i+1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i+1))
    print("====================================")
    print("Test script complete, Total points: %d" % points)
if __name__ == "__main__":
    main()