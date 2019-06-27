"""
Genetic Algorithm to try and solve the travelling salespererson problem
"""


from lexicographic_permutations import pop_cities, tot_distance, plot_cities, distance
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
# take half array of one and of the other (nice and simple to start of with)




def main():

    # interactive mode on
    plt.ion()

    # initialise the set of cities
    num_cities = 7

    cities = pop_cities(num_cities)
    # cities = [(0, 0), (1, 0), (0, 1), (1, 1)]

    print(cities)

    # create inital population of legnths
    new_pop = init_pop(cities, 10)

    while True:

        # get a score for the all the population elements
        new_pop = pop_score(new_pop)

        # debug
        # plot_best_dist(new_pop)
        print("Average population distance: {}".format(average_pop_score(new_pop)))

        # get a mating pool
        mat_pool = mating_pool(new_pop)

        # get the new population
        new_pop = create_new_pop(new_pop, mat_pool)



    return 0

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
        # pop["id"].append(perm)
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

# mate the objects and create new population
def create_new_pop(old_pop, mating_pool):
    """
    Get the new population from the old population and the mating pool
    """

    # population list which will contain all the different arrays of distance
    new_pop = {"path": []}

    # get a random set of n arrays
    while len(new_pop["path"]) < len(old_pop["path"]):

        # check if child is in the new_pop already
        while True:
            # choose at random from the mating pool two parents
            par1 = random.choice(mating_pool)
            par2 = random.choice(mating_pool)

            # create child
            child = new_ele(par1, par2)

            if child not in new_pop["path"]:
                break

        # place in pop list
        new_pop["path"].append(child)


    return new_pop

def new_ele(item1, item2):
    """
    Mate two elements from the population by getting half of 1 and half of the other
    """

    # you have to think of something more clever
    plt.ioff()

    item1 = np.array(item1)
    item2 = np.array(item2)

    print(item1, item2)

    x = item1[:, 0]
    y = item1[:, 1]


    x_2 = item2[:, 0]
    y_2 = item2[:, 1]

    plt.plot(x, y, "k--")
    plt.scatter(x, y, s = 25, c = "k")
    plt.plot(x_2, y_2, "r--")
    plt.show()


    new_item = [item1[0]]

    count = 0
    while new_item < len(item1):
        ele = item1[count]

        # get the position of the same element in item2
        pos_item2 = item2.index(ele)

        # get the distance from both items
        try:
            dist1 = distance(ele, item[count + 1])
        except error:
            dist1 = np.inf

        try:
            dist2 = distance(item2[pos_item2], item2[pos_item2 + 1])
        except:
            dist2 = np.inf


        if dist1 < dist2:
            new_item.append(item1[count + 1])
            count += 1
        else:
            new_item.appennd(item2[pos_item2 + 1])
            count = item1.index(item2[pos_item2 + 1])



    # get the two legnths of each item to be used
    len1 = int(len(item1)/ 2)

    # create new item
    new_item = item1[:len1] + item2[len1:]

    return new_item

def best_pop_score(pop):

    best = max(pop["score"])

    dist = 1 / best

    return dist

def average_pop_score(pop):

    distances = [1/pop["score"][i] for i in range(len(pop["score"]))]

    average = sum(distances) / len(distances)

    return average

def plot_population(pop):
    """
    Plot all the distances in the population
    """

    # plot the points of the cities
    cities = np.array(pop["path"][0])
    x = cities[:, 0]
    y = cities[:, 1]
    plt.scatter(x, y, s = 25, c = "k")

    for i in range(len(pop)):
        # get the x, y points
        cities = np.array(pop["path"][i])

        x_jour = cities[:, 0]
        y_jour = cities[:, 1]

        # plot points
        plt.plot(x_jour, y_jour)
        plt.axis('off')

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
    plt.plot(x_best, y_best, "r--")
    plt.axis('off')
    plt.show()
    plt.pause(2 * 1e-0)
    plt.clf()

    return None

def help():


    item1 = [1, 2 , 3, 4, 5]
    item2 = [4, 5, 6]


    try:
        a = item1[8]
        print(a)
    except error:
        print("over inddexed")

    return None


if __name__ == "__main__":
    start = time.time()
    # main()
    help()
    print("------------- Time taken: {} -----------------------------".format(time.time() - start))
