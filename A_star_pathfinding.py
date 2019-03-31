"""
A* path finding algorithm as in the coding train, intelligence and learning tutorial.
"""
from maze_creation import *

import numpy as np
import matplotlib.pyplot as plt
import time

see_path = True

def main():

    # define the number of cols and roes used in the porgram
    # global delta_x, rows, cols
    # rows  = 10
    # cols = 10
    # delta_x = 1

    # array contining a 2D array
    grid = main_maze()

    for cell in grid:
        cell.addNeighbours(grid)



    # defnine the closed and open set containing nodes to check and that have been checked
    openSet = []
    closedSet = []

    # start will be top left and end bottom right
    start = grid[index(0, 0)]
    end = grid[index(cols - 1, rows - 1)]
    openSet.append(start)


    # start algorithm
    while len(openSet) > 0:

        # start interactive mode
        plt.ion()

        # get the lowest f in the openSet
        winner = 0
        for i in range(len(openSet)):
            # ceck if it is smaller than the previous
            if openSet[i].f < openSet[winner].f:
                winner = i

        # get the lowest index
        current = openSet[winner]

        # find the path
        path = [current]

        #  get the current temporary node and loop backwards from this
        temp = current

        while temp.previous != None:
            # make  temp the previous spot and append it to the path
            temp = temp.previous
            path.append(temp)

        # check that if you hit the end youi are done
        if current == end:
            print("Done")

            # draw the path
            plt.ioff()
            draw(grid, "grid", "g")
            draw(path, "path", "r")
            plt.show()
            break

        # put the current set in closedSet and remove it from openSet
        closedSet.append(current)
        del openSet[winner]

        # new nodes I have to put in openSet
        # get the neighbours of current
        neighbours = current.neighbours

        # check every neighbour
        for neighbour in neighbours:
            # check if it is in the closed set
            if neighbour in closedSet:
                continue

            # temporary value of g to assign to the neighbour
            tempG = current.g + 1

            # check if you have evaluated it in the openset before?
            if neighbour in openSet:
                # check if you have gotten to it more quickly
                if tempG < neighbour.g:
                    # only now make it the lower g
                    neighbour.g = tempG

            # if not in open set put it in
            else:
                # change the value of g
                neighbour.g = tempG
                openSet.append(neighbour)

            # calculte the heuristic and f for the neighbour
            neighbour.h = heuristic(neighbour, end)
            neighbour.f = neighbour.g + neighbour.h

            # set the neighbours previous to current, hence it knows where it came from
            neighbour.previous = current


            # draw the grid
            if see_path == True:
                draw(grid, "grid", "g")
                draw(path, "path", "b")
                current.show("r")
                plt.show()
                plt.pause(1e-1)


    return 0

def heuristic(a, b):

    # get the x, y  components as its grid placing
    x_a = a.i
    y_a = a.j

    x_b = b.i
    y_b = b.j

    # get the euclideian distance
    # distance = ((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** ( 1/2)
    distance = abs(x_a - x_b) + abs(y_a - y_b)

    return distance


def help():


    return None

if __name__ == "__main__":
    start = time.time()
    main()
    # help()
    print("------------- Time taken: {} -----------------------------".format(time.time() - start))
