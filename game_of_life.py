# This is a simple terminal version of the game fo life
# import everything
import os
import random
from colorama import Back
white = Back.WHITE
black = Back.BLACK
# This function will be used to clear the terminal
clear = lambda: os.system('clear')

# Input WIDTH and HEIGHT
WIDTH = 189
HEIGHT = 99

# Setup
adj = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
grid = [[1 for i in range(WIDTH)] for i in range(HEIGHT)]

# Display grid in terminal
def display(grid):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j]: print(white + "  " + black, end = "")
            else: print("  ", end = "")
        print("")

# Calculate the next grid
def nextGrid(grid):
    tmp = [[0 for i in range(WIDTH)] for i in range(HEIGHT)]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            n_count = 0
            for e in adj:
                dx = e[0]
                dy = e[1]
                x = j + dx
                y = i + dy
                x = x % WIDTH
                y = y % HEIGHT
                if grid[y][x] == 1:
                    n_count += 1
            if grid[i][j] == 1:
                if n_count < 2:
                    tmp[i][j] = 0
                elif n_count > 3:
                    tmp[i][j] = 0
                else:
                    tmp[i][j] = 1
            else:
                if n_count == 3:
                    tmp[i][j] = 1
                else:
                    tmp[i][j] = 0
    return tmp
                
# random grid
def initialise_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            r = random.random()
            if r < 0.5:
                grid[i][j] = 0
            else:
                grid[i][j] = 1


# Initialise game
initialise_grid(grid)

# game loop
while True:
    display(grid)
    grid = nextGrid(grid)
    clear()

