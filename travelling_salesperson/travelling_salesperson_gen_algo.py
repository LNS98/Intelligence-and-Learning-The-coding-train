"""
Genetic Algorithm to try and solve the travelling salespererson problem
"""


from travelling_salesperson_lexi_order import pop_cities, tot_distance, plot_cities, distance, swap
import random
import numpy as np
import matplotlib.pyplot as plt

import time

# STRATEDGY

# what do I evolve??
# paths with a lower distance

# how do you score?
# well, the lower the distance the better, so (1/dist)^x.

# how do you initialsie population?
# create a set of random distances, they can be arrays

# how to mate?
# just pick better ones and mutate them



random.seed(0)


def main():

    # interactive mode on
    plt.ion()

    # initialise the set of cities
    num_cities = int(input("how many cities? "))

    cities = pop_cities(num_cities)
    # cities = [(0, 0), (1, 0), (0, 1), (1, 1)]

    genetic_algorithm_implementation(cities)

    return 0

def genetic_algorithm_implementation(cities, show_graph = True):

    # create inital population of legnths
    new_pop = init_pop(cities, 50)

    # initialise the best distance as the first one
    best_dist = tot_distance(cities)
    best_path = cities.copy()

    while True:

        # get a score for the all the population elements
        new_pop = pop_score(new_pop)

        # debug
        # print("Average population distance: {}".format(average_pop_score(new_pop)))
        # print("Best population distance: {}\n".format(best_pop_score(new_pop)))

        # check to see if there is a better path
        best_pop_distance = best_pop_score(new_pop)

        # update best distnace if current is lower
        if best_pop_distance < best_dist:
            if show_graph == True:
                plot_best_dist(new_pop)

            # get the best path and distance
            best_dist = best_pop_distance
            best_path = cities.copy()

            print(best_dist)


        # get a mating pool
        mat_pool = mating_pool(new_pop)

        # get the new population
        new_pop = create_new_pop(new_pop, mat_pool)

    return None

# ------------------------------- Genetic Algorithm -----------------------

# initialise the set of arrays used in first population
def  init_pop(init_array, n):
    """
    Create an initial population made of n elements.
    """

    # population list which will contain all the different arrays of distance
    pop = {"path": []}

    # print(init_array)

    # get a random set of n arrays
    while len(pop["path"]) < n:
        # get a random permuation
        perm = shuffle(len(init_array))
        rand_array = [init_array[j] for j in perm]

        # place in pop list
        # pop["order"].append(perm)
        pop["path"].append(rand_array)

    return pop

def shuffle(n):
    """
    get a set of random numbers up to n
    """

    permutation = [i for i in range(n)]
    random.shuffle(permutation)

    return permutation

# calculate the score for each element in pop

def pop_score(pop):
    """
    return a dictionary containing array and score for the population
    """

    # initialise the score coloumn
    pop["score"] = []

    for element in pop["path"]:
        # get the score of the element
        score = element_score(element)
        # append to the dictionary
        pop["score"].append(score)

    return pop

def element_score(array):
    """
    calculate the score on a individual array as 1/dist
    """
    distance = tot_distance(array)

    score = 1 / distance

    return score

# create mating pool weighting by inverse distance score
def mating_pool(pop):
    """
    create a list contining the weighted values of the pop given the score values
    """

    mating_pool = []

    # loop over each element in teh score element of pop
    for element, score in zip(pop["path"], pop["score"]):
        # multiply the score by 1000 and add that many values to the mating pool
        mating_pool += int(score * 1000) * [element]

    return mating_pool

def mutate(array, mut_rate):
    """
    Swap the order of two elements in the array
    """
    # create a copy of the order which you will mutate
    new_order = array

    # get a ranndom number in the order array
    rand_index = random.randint(0, len(array))

    # in this case no mutation because it has randomly selected the last element
    if rand_index >= len(array) - 1:
        return array

    # only mutate accorading to the mutation rate
    if random.random() > mut_rate:
        return array

    # swap the index of the random number and the next one in the array
    swap(new_order, rand_index, rand_index + 1)

    return new_order

# mate the objects and create new population
def create_new_pop(old_pop, mating_pool):
    """
    Get the new population from the old population and the mating pool
    """

    # population list which will contain all the different arrays of distance
    new_pop = {"path": []}

    # get a random set of n arrays
    while len(new_pop["path"]) < len(old_pop["path"]):


        # choose at random from the mating pool two parents
        parent = random.choice(mating_pool)

        # create child by mutating parent
        child = mutate(parent, 0.1)

        # place in pop list
        new_pop["path"].append(child)


    return new_pop

def best_pop_score(pop):

    best = max(pop["score"])

    dist = 1 / best

    return dist

def average_pop_score(pop):

    distances = [1/pop["score"][i] for i in range(len(pop["score"]))]

    average = sum(distances) / len(distances)

    return average

# --------------------------------- Plot the graphs --------------------

def plot_population(pop):
    """
    Plot all the distances in the population
    """

    # plot the points of the cities
    cities = np.array(pop["path"][0])
    x = cities[:, 0]
    y = cities[:, 1]
    plt.scatter(x, y, s = 25, c = "k")

    for i in range(len(pop["path"])):
        # get the x, y points
        cities = np.array(pop["path"][i])

        x_jour = cities[:, 0]
        y_jour = cities[:, 1]

        # plot points
        plt.plot(x_jour, y_jour, "--")
        # plt.axis('off')

    plt.show()

    return None

def plot_best_dist(pop):
    """
    Plot the best distance of the population
    """

    # plot the points of the cities
    cities = np.array(pop["path"][0])
    x = cities[:, 0]
    y = cities[:, 1]
    plt.scatter(x, y, s = 25, c = "k")

    # get the best path
    best_score = max(pop["score"])
    best_index = pop["score"].index(best_score)
    best_path = np.array(pop["path"][best_index])

    x_best = best_path[:, 0]
    y_best = best_path[:, 1]

    # plot points
    plt.plot(x_best, y_best, "k-")
    plt.axis('off')
    plt.show()
    plt.pause(2 * 1e-7)
    plt.clf()

    return None

def help():


    cities = pop_cities(3)
    # cities = [(0, 0), (1, 0), (0, 1), (1, 1)]

    # create inital population of legnths
    new_pop = init_pop(cities, 2)

    print(new_pop)

    # make a child out of the  population
    child = new_ele_try2(new_pop["path"][0], new_pop["path"][1])

    # plot the population
    plot_population(new_pop)

    return None


if __name__ == "__main__":
    start = time.time()
    main()
    # help()
    print("------------- Time taken: {} -----------------------------".format(time.time() - start))
