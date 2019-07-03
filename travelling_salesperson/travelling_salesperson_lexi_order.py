"""
Lexico travelling salesperson algorithm implementation. Basically check all the
permutations
"""



import matplotlib.pyplot as plt
import time
from lex_graph_order import algorithm as lex_order

import random
import numpy as np

random.seed(0)

def main():

    # interactive mode on
    plt.ion()

    # decide how many cities to have
    num_cities = int(input("how many cities? "))

    # initlialise the array which will contain the cities for which eh path has to be checcked
    cities = pop_cities(num_cities)

    # debug puposes
    # cities = [(0, 0), (1, 0), (0, 1), (1, 1)]

    lexi_algorithm(cities)

    return None

def lexi_algorithm(cities, show_graph = True):
    """
    the algorithmfor the Lexicographical implementation of the travelling
    salesperson.
    """

    # initialise the best distance as the first one
    best_dist = tot_distance(cities)
    best_path = cities.copy()

    while True:

        # display cities
        if show_graph == True:
            plot_cities(cities, best_path)

        # get the next order of teh cities using lex order
        prev_cities = cities
        cities = lex_order(cities)

        # stop if you've gone through all teh permutations
        if cities == False:
            plt.ioff()
            # display cities
            print("Finished")
            plot_cities(prev_cities, best_path)
            break

        # check the new distance
        curr_dist = tot_distance(cities)

        # update best distnace if current is lower
        if curr_dist < best_dist:
            # get the best path and distance
            best_dist = curr_dist
            best_path = cities.copy()


            print(best_dist)


    return None

def pop_cities(num_cities):
    """
    Return an array  with the x, y location of the number of cities.
    """

    # initialise empty array which will contain cities
    cities  = []

    for i in range(num_cities):
        # get a random x, y point between 0, 10
        x = random.random() * 10
        y = random.random() * 10

        # append as an array to the cities
        cities.append((x, y))

    return cities

def swap(array, i, j):
    """
    Swap position i and j in the array
    """

    temp = array[i]

    array[i] = array[j]
    array[j] = temp

    return None

def distance(a, b):
    """
    calculate the distance between points a and b.
    """
    x_dist = b[0] - a[0]
    y_dist = b[1] - a[1]

    dist = (x_dist ** 2 + y_dist ** 2) ** (1/2)

    return dist

def tot_distance(points):
    """
    Calculate the distance between the points in the incoming array.
    """
    # initialise total sum
    sum = 0

    # loop along points
    for i in range(len(points) - 1):
        # get the ith and ith + 1 point
        a = points[i]
        b = points[i + 1]

        # add the distance to the sum
        sum += distance(a, b)


    return sum

def plot_cities(cities, best_path):

    # get the x, y points
    cities = np.array(cities)

    x = cities[:, 0]
    y = cities[:, 1]

    best_path = np.array(best_path)

    x_best = best_path[:, 0]
    y_best = best_path[:, 1]

    # plot points
    plt.scatter(x, y, s = 25, c = "k")
    plt.plot(x, y, "r--")
    plt.plot(x_best, y_best, "k-")
    plt.axis('off')
    plt.show()
    plt.pause(2 * 1e-5)
    plt.clf()

    return None

def help():

    a = [1, 2, 4, 5]
    print(a)

    swap(a, 2, 3)

    print(a)

    return None

if __name__ == "__main__":
    start = time.time()
    main()
    # help()
    print("------------- Time taken: {} -----------------------------".format(time.time() - start))
