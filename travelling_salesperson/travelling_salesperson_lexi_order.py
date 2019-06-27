"""
Implement the Lexicographical order Algorithm. An example of this is: for A,B,C
the order would be: ABC, ACB, BAC, BCA, CAB, CBA.
"""

import numpy as np
import time

def main():

    # initialise test array
    new_array = [0, 1, 2, 3]

    while new_array != False:
        print(new_array)
        new_array = algorithm(new_array)


    return 0

def algorithm(array):
    """
    1) Find largest x : p[x] < p[x + 1]. If you cant this is the last permutation
    2) Find largest y : p[x] < p[y].
    3) Swap p[x] and p[y]
    4) Reverse p[x+1 .. n]
    """

    # Do step 1 by finding largest X value
    largest_x = None # this is an invalid index
    for i in range(len(array) - 1):
        # check for p[x] < p[x+1]
        if array[i] < array[i + 1]:
            largest_x = i

    if largest_x == None:
        return False

    # find largest y : p[x] < p[y]
    largest_y = None
    for j in range(len(array)):
        if array[largest_x] < array[j]:
            largest_y = j

    if largest_y == None:
        return False

    # swap p[x] and p[y]
    temp = array[largest_x]
    array[largest_x] = array[largest_y]
    array[largest_y] = temp

    # reverse p[x+1, ... , n]
    reverse_array = array[:largest_x:-1]
    new_array = array[:largest_x + 1] + reverse_array

    return new_array

def help():

    a = [1, 2, 3, 4 ,5, 6]

    # reverse p[x+1, ... , n]
    new_array = a[:3]

    print(new_array)


    return None

if __name__ == "__main__":
    start = time.time()
    main()
    # help()
    print("------------- Time taken: {} -----------------------------".format(time.time() - start))
