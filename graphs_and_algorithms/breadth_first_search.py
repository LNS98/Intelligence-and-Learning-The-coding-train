"""
Make a breadth-search algorithm following the playlist by the coding train on intelligence and learning.
The algorithm works by basically checking all the neighbours to a given node to see if result is found
working through all the edges and nodes with a queue data structure.
"""


import json



def main():

    #################### load data ####################

    # set up the problem by loading sample data
    with open("kevinbacon.json", "r") as read_file:
        data = json.load(read_file)

    # make a graph object
    gra = Graph()

    # get the movies and make a movie a new node
    movies = data["movies"]


    for movie in movies:
        cast = movie["cast"]

        movieNode = Node(movie["title"])
        gra.addNode(movieNode)

        # now put the actors in
        for actor in cast:
            # check if graph already contains actor
            actorNode = gra.getNode(actor)
            if actorNode == None:
                actorNode = Node(actor)

            gra.addNode(actorNode)

            # add the edeges of the graph
            movieNode.addEdge(actorNode)

    ############################# start bread-search algorithm ######################

    start = gra.setStart("Rachel McAdams")
    end = gra.setEnd("Kevin Bacon")


    # initilise queue
    q = []

    # start has been searhced and add to que
    start.searched = True
    q.append(start)

    # repeat until q is empty
    while len(q) > 0:
        # get the first item from the que
        current = q.pop(0)

        # if currnet is the goal we are done!
        if current == end:
            print("Found {} !!!!".format(current.value))
            break
        # get the edges of the current node
        edges = current.edges

        # check through all the edges
        for edge in edges:
            # check if it has been searched
            if edge.searched == False:
                edge.searched = True
                # set its parrent to current value
                edge.parent = current
                # put it in the queue
                q.append(edge)

    # now lets find the path to end
    path = []

    #  start at end
    path.append(end)

    # get the first parent
    next = end.parent
    # loop until start in which case parent is None
    while next != None:
        path.append(next)
        # change next to new next
        next = next.parent

    for i in range(len(path)):
        reverse_i = len(path) - 1 - i
        print(path[reverse_i].value, end = "")
        if reverse_i != 0:
            print (" ---> ", end = "")

    return 0



class Node:

    def __init__(self, value):
        # initialise the values
        self.value = value
        self.edges = []
        self.searched = False
        self.parent = None


    def addEdge(self, neighbour):
        self.edges.append(neighbour)
        # put edges both ways
        neighbour.edges.append(self)

        return None

    def vis_edges(self):
        print("\n")
        print(self.value)
        for edge in self.edges:
            print(edge.value)

        return None
# keep trach of all nodes
class Graph:

    def __init__(self):
        self.nodes = []
        self.graph = {}
        self.start = None
        self.end = None

    def addNode(self, node):
        # put the node in the list of nodes
        self.nodes.append(node)

        # get a key for the incoming node and place the key and graph in the graph
        title = node.value

        # node into "hash"
        self.graph[title] = node

        return None

    def getNode(self, actor):
        try:
            # get the actor from graph
            n = self.graph[actor]
        except:
            n = None

        return n

    def setStart(self, actor):
        self.start = self.graph[actor]

        return self.start

    def setEnd (self, actor):
        self.end = self.graph[actor]

        return self.end


def help():
    sample = [1, 2, 4, 5]
    first = sample.pop()
    print(first)
    print(sample)

    return 0

if __name__ == "__main__":
    main()
    # help()
