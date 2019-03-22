"""
Maze Generation algoithm as in the training code challenge from intelligence and learning tutorial.
"""

import matplotlib.pyplot as plt
import random
import time

def main():

    # define the gloabal variables for the problem
    global delta_x, rows, cols
    rows  = 10
    cols = 10
    delta_x = 1


    # make an array containing all the grid points and the stack
    grid = []
    stack = []

    # create all the cells in the grid
    for i in range(rows):
        # go through rows
        for j in range(cols):
            # go through columns
            # make a cell
            cell = Cell(i, j)
            grid.append(cell)

    # draw grid
    # draw(grid)

    #---------------------- Start algorithm --------------------------

    # set a current cell being looked at, start at top left for simplicity
    current = grid[index(0, 0)]
    # set it to visited
    current.visited = True

    while True:

        # start interactive mode
        plt.ion()


        # get a random unvisited neighbour
        next = current.checkNeighbours(grid)

        if next == None and len(stack) == 0:
            # program ended
            plt.ioff()
            draw(grid)
            plt.show()
            break


        if next != None:

            # place the next cells to the stack
            stack.append(next)

            # now it has been visited
            next.visited = True

            # remove walls between the two cells
            current, next = removeWalls(current, next)

            # set current to next
            current = next

        elif next == None and len(stack) > 0:
            # get the cell from the stack
            current = stack.pop()

        else:
            # program ended
            plt.ioff()
            draw(grid)
            plt.show()
            break


        # draw grid
        draw(grid)
        # show figure
        plt.show()
        plt.pause(1e-3)
        plt.clf()

    return 0

def index(i, j):
    # check if its a valid index in the grid
    if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
        return None

    return j + cols*i

def removeWalls(a, b):

    # find which walls is between the a and b cells

    # get the difference between the cells
    delta_i = b.i - a.i
    delta_j = b.j - a.j

    # if delta is +1 then corresponds to bottom/ top
    if delta_i == 1:
        a.walls[1] = False
        b.walls[3] = False

    # if delta is -1 then corresponds to bottom/ top
    if delta_i == -1:
        a.walls[3] = False
        b.walls[1] = False

    # if delta is +1 then corresponds to right/ left
    if delta_j == 1:
        a.walls[2] = False
        b.walls[0] = False

    # if delta is -1 then corresponds to left/ right
    if delta_j == -1:
        a.walls[0] = False
        b.walls[2] = False

    return a, b


def draw(grid):
    """
    Draw the grid
    """

    # create all the cells in the grid
    for i in range(rows):
        # go through rows
        for j in range(cols):
            cell = grid[index(i, j)]
            # show the grid made
            cell.show()

    return None


class Cell:

    def __init__(self, i, j):
        # row number (y's) (centre of x,y coordinates)
        self.i = i
        # cloumn number (x's) (centre of x,y coordinates)
        self.j = j
        # initilaise each walls with all sides being walls
                    # bottom, right, top, left
        self.walls = [True, True, True, True]
        # check if cell has been visited, at start it is not visited
        self.visited = False

    def checkNeighbours(self, grid):
        # initilise a empty areay which will contain the neighbours
        neighbours = []

        # get the bottom, right, top, left neighbours
        bottom = index(self.i - 1, self.j)
        right = index(self.i, self.j + 1)
        top = index(self.i + 1, self.j)
        left = index(self.i, self.j - 1)

        # list of indicies
        indicies = [bottom, right, top, left]

        for index_value in indicies:
            if index_value != None:
                # get the grid value of the neighbour
                grid_value = grid[index_value]
                if grid_value.visited == False:
                    #if not visited
                    neighbours.append(grid_value)

        # pick a random neighbour
        if len(neighbours) > 0:
            return random.choice(neighbours)

        return None


    def show(self):

        # x cooridnates
        left_x = self.i - delta_x / 2
        right_x = self.i + delta_x / 2
        # y coordinates
        down_y = self.j - delta_x / 2
        up_y = self.j + delta_x / 2

        # plot each line, not a rectangle: one plot is a wall of the "maze"
        # print(sel f.walls)

        #plot only if walls  exisit
        if self.walls[0] == True:
            plt.plot([left_x, right_x], [down_y,down_y], "k-")
        if self.walls[1] == True:
            plt.plot([right_x, right_x], [down_y, up_y], "k-")
        if self.walls[2] == True:
            plt.plot([right_x, left_x], [up_y, up_y], "k-")
        if self.walls[3] == True:
            plt.plot([left_x, left_x], [up_y, down_y], "k-")


        if self.visited == True:
            # plot circling the whole cell
            plt.fill([left_x, right_x, right_x, left_x, left_x],
                     [down_y,down_y, up_y, up_y, down_y], "g")

        # plot circling the whole cell
        # plt.fill([left_x, right_x, right_x, left_x, left_x],
        #          [down_y,down_y, up_y, up_y, down_y], "g")
        return None

def help():

    hello = [1, 2, 3]

    a = hello.pop()

    print(a)
    print(hello)

    return None

if __name__ == "__main__":
    main()
    # help()
