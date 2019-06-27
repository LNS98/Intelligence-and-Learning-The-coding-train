"""
Make a binary search tree following the playlist by the coding train on binary search tree
"""

# binary tree is a divide and conquer approach
# nodes with always two children node.

from random import randint

def main():

    # initialse the tree
    bin_tree = Tree()

    # add the node as the root tree
    for i in range(10):
        value = randint(0, 10)
        bin_tree.addNodeTree(value)


    # print the sorted tree
    bin_tree.traverse()
    # search
    bin_tree.search_tree(3)

    return 0


# define the tree class/object
class Tree:

    def __init__(self):
        self.root = None

    def visualise(self):
        # visulaise rest of the tree
        self.root.visualise()

        return None

    def traverse(self):
        self.root.visit()
        return None

    def addNodeTree(self, n):
        n = Node(n)
        if self.root == None:
            self.root = n
        else:
            self.root.addNode(n)
        return None

    def search_tree(self, value):

        node = self.root.search(value)

        if node == None:
            print("Not Found!")
        else:
            print("Found!")
        return None

# define a class for the nodes of the tree
class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def visualise(self):
        print("Value of node: {}".format(self.value))

        if self.left != None:
            self.left.visualise()

        if self.right != None:
            self.right.visualise()

        if self.left == None and self.right == None:
            print("End of Tree")

        return None

    def addNode(self, node):
        n = node.value
        if n < self.value:
            if self.left == None:
                self.left = node
            else:
                self.left.addNode(node)
        if n > self.value:
            if self.right == None:
                self.right = node
            else:
                self.right.addNode(node)

        return None

    def visit(self):
        # check the left nodes
        if self.left != None:
            self.left.visit()

        # print the left most value
        print(self.value)

        # check the right nodes
        if self.right != None:
            self.right.visit()

        return None

    def search(self, value):
        n = self.value

        # if equal to the value print it
        if value == n:
            return self

        # if value is smaller than node value go left
        if value < n:
            if self.left != None:
                return self.left.search(value)


        # if value id bigger check the right
        if value > n:
            if self.right != None:
                return self.right.search(value)

        return None


if __name__ == "__main__":
    main()
