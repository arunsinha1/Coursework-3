import time
import csv
import copy
import matplotlib.pyplot as plt
import numpy as np

# Grids 1-5 are 2x2

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

#grid6 is 2x3

grid6 = [
		[0, 0, 6, 0, 0, 3],
		[5, 0, 0, 0, 0, 0],
		[0, 1, 3, 4, 0, 0],
		[0, 0, 0, 0, 0, 6],
		[0, 0, 1, 0, 0, 0],
		[0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2),(grid6,2,3)]

'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''

def start():

    #intialising variables
    global profile, hint, explain, file, input_file, output_file, number_of_hints
    input_file, output_file = "",""
    profile, hint, explain, file = False, False, False, False
    number_of_hints = 100

    print("====================================")
    user_input = input('''Welcome to our code for Coursework 3!
Please input how you would like the code to be run using the instructions below:
"-explain" will provide a set of instructions for solving the puzzle (i.e as a list of commands such as “Put 2 in location (3, 4)”
"-file" will read a grid from a file (specified with the first argument), solves it, and then saves the solution to another file (specified as OUTPUT)
"-hint N" where N is a number, rather than giving the full solution, instead returns a grid with N values filled in.
"-profile" measures the performance of your solver(s) (in terms of time) for grids of different size (2x2, 3x2, 3x3) and difficulties (specified by number of unfilled locations). This should average the performance over a few solution attempts and starting conditions, summarising the results as a plot(s)
Note: you can input multiple things! Just seperate them using '-'
''')

    #purifying user's input
    file_details =copy.copy(user_input)
    user_input = user_input.replace(" ","")
    user_input = user_input.split("-")

    #determining what the user inputted and changing flags accordingly
    for n in range(len(user_input)):
        if "profile" in user_input[n]:
            profile = True
            hint, explain, file = False, False, False
        if profile==False:
            if "explain" in user_input[n]:
                explain = True
            if "hint" in user_input[n]:
                number_of_hints = [str(i) for i in user_input[n] if i.isdigit()]
                number_of_hints = ''.join(number_of_hints)
                index = user_input.index("hint"+str(number_of_hints))
                user_input[index] = "hint"
                hint = True
            if "file" in user_input[n]:
                file_details = file_details.split(" ")
                for i in range(len(file_details)):
                    file_details[i] = file_details[i].replace(" ","")
                    file_details[i] = file_details[i].replace("-","")
                index = file_details.index("file")
                del (file_details[:index])
                if file_details[0] == "file":
                    input_file = file_details[1]
                    output_file = file_details[2]
                    file = True

    return(explain,file,hint,profile,number_of_hints, input_file, output_file)

def import_file():

    global m
    #opening the file which contains the grid that the user wants to solve
    with open('grids/'+input_file+'.txt') as f:
        #storing the file details as a grid
        m = csv.reader(f)
        m = list(m)
        m = [[(int(m[i][j])) for j in range(len(m[i]))] for i in range(len(m))]
    return(m)

def export_file(solution):

    #opening a new file and printing the soolution to the grid that the user wants to solve
    with open('grids/solutions/'+output_file+".txt", 'w',) as f:
        f.write("This is the solved solution for "+ input_file+"\n")
        #loop to print the grid in a aesthetically pleasing format
        for i in range(len(solution)): f.write(str(solution[i])+"\n")

        
def check_section(section, n):

    #check if a single section of the grid is correct
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(n+1)]): return True
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
        if check_section(row, n) == False: return False
    for i in range(n_rows**2):
        column = []
        for row in grid: column.append(row[i])
        if check_section(column, n) == False: return False
    squares = get_squares(grid, n_rows, n_cols)
    for square in squares:
        if check_section(square, n) == False: return False
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
            if grid[i][j] == 0: return (i, j)

    return None

def find_all_empty_spaces_spaces(grid):
    '''
    This function returns the index (i, j) to the first zero element in a sudoku grid
    If no such element is found, it returns None
    args: grid
    return: A tuple (i,j) where i and j are both integers, or None
    '''
    
    global all_empty_spaces
    all_empty_spaces=[]
    
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == 0:
                empty=(i,j)
                all_empty_spaces.append(empty)
    
    if len(all_empty_spaces) == 0:
        return None
    else:
        return(i,j)
    
def recursive_solve(number_of_hints, recursive_function_called, grid, n_rows, n_cols):
    '''
    This function uses recursion to exhaustively search all possible solutions to a grid
    until the solution is found
    args: grid, n_rows, n_cols
    return: A solved grid (as a nested list), or None
    '''
    
    #n is the maximum integer considered in this board
    n = n_rows*n_cols
    #set which stores the possible numbers which can go in the empty space
    possible_numbers=set(list(range(1, n+1)))
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
    possible_numbers = possible_numbers - set(grid[empty[0]])
    possible_numbers = possible_numbers - set(grid[i][empty[1]] for i in range(len(grid)))
    square_row, square_col = empty[0] // n_rows, empty[1] // n_cols
    for i in range(square_row * n_rows, (square_row + 1) * n_rows):
        for j in range(square_col * n_cols, (square_col + 1) * n_cols):
            possible_numbers.discard(grid[i][j])
    
    #loop through the possible values
    for i in possible_numbers:
        #Place the value into the empty space in the grid
        grid[empty[0]][empty[1]] = i
        #if the user wants an explanation, this prints out a set of instructions
        
        if explain == True:
            #this condition ensures each step is only printed once
            if recursive_function_called not in explain_count:
                explain_count.append(recursive_function_called)
                #prints the instruction step to fill the grid
                print(str(recursive_function_called)+ ". Put the value",i , "in the position (" + str(empty[0]) +","+ str(empty[1]) + ")")
    
        #if the user wants some values filled in, this condition allows that to happen
        if hint==True:
            #this checks if filling in the number of values the user wants, fills the grid completely
            find_all_empty_spaces_spaces(grid)
            #this prints the completed grid if the hint number is larger than the number of empty spaces
            if len(all_empty_spaces) == 0 and recursive_function_called<int(number_of_hints):
                print(grid)
            #this condition checks if the number of hints has been filled
            if recursive_function_called==int(number_of_hints):
                #this condition ensures that the grid is only printed once
                if recursive_function_called not in hint_count:
                    hint_count.append(recursive_function_called)
                    #these let the user know what is happening
                    if explain==True:
                        print("\nThese", recursive_function_called,"values shown above have already been filled in for you\n")
                    else:
                        print(recursive_function_called,"values have been filled in for you")
                    for i in range((len(grid))):
                        print(grid[i])
                    print("\n")
        
        #this helps us know how many times the recursive function has been called
        recursive_function_called+=1
        
        #recursively call the function
        ans = recursive_solve(number_of_hints, recursive_function_called,grid, n_rows, n_cols)
        
        #if the user doesn't want a specific number of spaces filled, just fill the grid completely
        if hint==False:
            #If we've found a solution, return it
            if ans:
                return ans
        
        # If we couldn't find a solution, that must mean this value is incorrect
        #Reset the grid for the next iteration of the loop
        grid[empty[0]][empty[1]] = 0 
   
    #If we get here, we've tried all possible values. Return none to indicate the previous value is incorrect.
    return None

def solve(number_of_hints, grid, n_rows, n_cols):
    '''
    Solve function for Sudoku coursework.
    Comment out one of the lines below to either use the random or recursive solver
    '''    
    
    #these control how many times the function is called
    recursive_function_called=1
    global explain_count, hint_count
    explain_count, hint_count =[],[]
    
    
    return recursive_solve(number_of_hints, recursive_function_called, grid, n_rows, n_cols)

def plots(number_of_hints, grid, n_rows, n_cols):
    
    grid1 = [
            [1, 0, 4, 2],
            [4, 2, 1, 3],
            [2, 1, 3, 4],
            [3, 4, 2, 1]]
    grid2 = [
            [1, 0, 4, 2],
            [0, 2, 1, 0],
            [2, 1, 0, 4],
            [0, 4, 2, 1]]
    grid3 = [
    		[1, 2, 6, 5, 4, 3],
    		[5, 3, 4, 6, 2, 1],
    		[6, 1, 3, 4, 5, 2],
    		[2, 4, 5, 3, 1, 6],
    		[0, 0, 1, 0, 0, 0],
    		[0, 5, 0, 0, 6, 4]]
    grid4 = [
            [0, 3, 0, 4, 0, 0],
            [0, 0, 5, 6, 0, 3],
            [0, 0, 0, 1, 0, 0],
            [0, 1, 0, 3, 0, 5],
            [0, 6, 4, 0, 3, 1],
            [0, 0, 1, 0, 4, 6]]
    grid5 = [
            [9, 8, 6, 3, 5, 1, 2, 4, 7],
            [7, 3, 1, 2, 9, 4, 8, 6, 5],
            [4, 0, 2, 8, 0, 6, 3, 0, 0],
            [0, 0, 0, 0, 2, 0, 9, 8, 0],
            [6, 7, 8, 4, 3, 9, 5, 1, 2],
            [0, 9, 4, 0, 8, 0, 0, 0, 0],
            [0, 0, 3, 7, 0, 8, 4, 0, 9],
            [0, 4, 0, 0, 1, 3, 7, 0, 6],
            [0, 6, 0, 9, 0, 0, 1, 0, 8]]   

    grid6 = [
            [0, 2, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 6, 0, 4, 0, 0, 0, 0],
            [5, 8, 0, 0, 9, 0, 0, 0, 3],
            [0, 0, 0, 0, 0, 3, 0, 0, 4],
            [4, 1, 0, 0, 8, 0, 6, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 9, 5],
            [2, 0, 0, 0, 1, 0, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 3, 1, 0, 0, 8, 0, 5, 7]]
    
    grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 3), (grid4, 2, 3), (grid5, 3, 3),(grid6,3,3)]
    
    time_plot=[]
    x=0
    y=[]
    
    for n in range(1000):
        temporary=[]
        for (i, (grid, n_rows, n_cols)) in enumerate(grids):
            start_time = time.time()
            solution = solve(number_of_hints, grid, n_rows, n_cols)
            elapsed_time = time.time() - start_time
            temporary.append(elapsed_time)
        time_plot.append(temporary)
    
    for n in range(len(time_plot[0])):
        for i in range(len(time_plot)):
            x= x+time_plot[i][n]
        y.append(x)
    
    return(y)
    
'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''

def main():
    points = 0
    solve_time = []
    print("Running test script for coursework 3")
    start()
    #if user wants to solve their own grid, add it to grids and remove the others
    if file == True:
        import_file()
        if input_file == "easy3":
            i=(m,2,3)
            grids.append(i)
        else:
            i =(m,3,3)
            grids.append(i)
        index = grids.index(i)
        del grids[:index]
    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("\nSolving grid: %d \n" % (i+1))
        if explain==True:
            print("Here are a set of instructions to help you solve the grid")
        start_time = time.time()
        solution = solve(number_of_hints, grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        solve_time.append(elapsed_time)
        if hint == False:
            print("\nSolved in: %f seconds" % elapsed_time)
            for i in range(len(solution)):
                print(solution[i])
            if check_solution(solution, n_rows, n_cols):
                print("grid %d correct" % (i+1))
                points = points + 10
            else:
                print("grid %d incorrect" % (i+1))
    if file == True:
        print("The solution for your requested grid has been saved to the folder named 'solutions'")
        export_file(solution)
    print("====================================")
    print("Test script complete, Total points: %d" % points)
    #this condition checks if the user wants a plot of solve time
    
    
    if profile==True:
    
        
        time_plot = plots(number_of_hints, grid, n_rows, n_cols)
        recursive_plots = ("recursive 2x2 solver","recursive 2x3 solver","recursive 3x3 solver")
        size = {
            'Simple Grid': (time_plot[0],time_plot[2],time_plot[4]),
            'Complex Grid': (time_plot[1],time_plot[3],time_plot[5]),
        }
        
        x = np.arange(len(recursive_plots))  # the label locations
        width = 0.25  # the width of the bars
        multiplier = 0.5
        
        fig, ax = plt.subplots(layout='constrained')
        
        for attribute, measurement in size.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3, rotation = 90)
            multiplier += 1
    
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Solve Time in Seconds')
        ax.set_title('Comparison of Solve Time')
        ax.set_xticks(x + width, recursive_plots)
        ax.legend(labels=['Easy Difficulty','Hard Difficulty'])
        #print bar chart
        plt.show()
        
if __name__ == "__main__": main()