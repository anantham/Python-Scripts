# Implementation of Kruskal's Algorithm

# this is a greedy algorithm to find a MST (Minimum Spanning Tree) of a given connected, undirected graph. graph

# So I am implementing the graph using adjacency list, as the user wont be
# entering too many nodes and edges.The adjacency matrix is a good implementation
# for a graph when the number of edges is large.So i wont be using that here

# Vertex, which will represent each vertex in the graph.Each Vertex uses a dictionary
# to keep track of the vertices to which it is connected, and the weight of each edge. 
class Vertex:

    # Initialze a object of this class
    # we use double underscore 
    def __init__(self, key):
        # we identify the vertex with its key
        self.id = key
        # this stores the info about the various connections any object 
        # (vertex) of this class has using a dictionary which is called connectedTo.
        # initially its not connected to any other node so,
        self.connectedTo={}

    # Add the information about connection between vertexes into the dictionary connectedTo
    def addNeighbor(self,neighbor,weight=0):
        # neighbor is another vertex we update the connectedTo dictionary ( Vertex:weight )
        # with the information of this new Edge, the key is the vertex and
        # the edge's weight is its value. This is the new element in the dictionary
        self.connectedTo[neighbor] = weight

    # Return a string containing a nicely printable representation of an object.
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # Return the vertex's self is connected to in a List
    def getConnections(self):
        return self.connectedTo.keys()

    # Return the id with which we identify the vertex, its name you could say
    def getId(self):
        return self.id

    # Return the value (weight) of the edge (or arc) between self and nbr (two vertices)
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

# The Graph class contains a dictionary that maps vertex keys to vertex objects (vertlist) and a count of the number of vertices in the graph
class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0


    # Returns a vertex which was added to the graph with given key
    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        # create a vertex object
        newVertex = Vertex(key)
        # set its key
        self.vertList[key] = newVertex
        return newVertex

    # Return the vertex object corresponding to the key - n
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    # Returns boolean - checks if graph contains a vertex with key n
    def __contains__(self,n):
        return n in self.vertList

    # Add's an edge to the graph using addNeighbor method of Vertex
    def addEdge(self,f,t,cost=0):
        # check if the 2 vertices involved in this edge exists inside
        # the graph if not they are added to the graph
        # nv is the Vertex object which is part of the graph
        # and has key of 'f' and 't' respectively, cost is the edge weight
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        # self.vertList[f] gets the vertex with f as key, we call this Vertex
        # object's addNeighbor with both the weight and self.vertList[t] (the vertice with t as key) 
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    # Return the list of all key's corresponding to the vertex's in the graph
    def getVertices(self):
        return self.vertList.keys()

    # Returns an iterator object, which contains all the Vertex's
    def __iter__(self):
        return iter(self.vertList.values())
    


# Now lets make the graph
the_graph=Graph()

print "enter the number of nodes in the graph"
no_nodes=int(raw_input())

# setup the nodes
for i in range(no_nodes):
    print "enter the Node no:"+str(i+1)+"'s key"
    the_graph.addVertex(raw_input())

print "enter the number of edges in the graph"
no_edges=int(raw_input())


# setup the edges
for i in range(no_edges):
    print "For the Edge no:"+str(i+1)
    print "of the 2 nodes involved in this edge \nenter the first Node's key"
    node1_key=raw_input()
    print "\nenter the second Node's key"
    node2_key=raw_input()
    print "\nenter the cost (or weight) of this edge (or arc) - an integer"
    cost=int(raw_input())
    # add the edge with this info
    the_graph.addEdge(node1_key,node2_key,cost)
    the_graph.addEdge(node2_key,node1_key,cost)

print "enter the maximum weight possible for any of edges in the graph"
max_weight=int(raw_input())

# graph DONE - start MST finding

# step 1 : Take all edges and sort them

#  Time Complexity of Solution:
#  Best Case O(n+k); Average Case O(n+k); Worst Case O(n+k),
#  where n is the size of the input array and k means the
#  values(weights) range from 0 to k.
def counting_sort(weights,max_weight):
    # these k+1 counters are made here is used to know how many times each value in range(k+1) (0 to k) repeats
    counter=[0]*(max_weight+1)
    for i in weights:
        # if you encounter a particular number increment its respective counter
        counter[i] += 1
    # no idea why ndx?! it is the key for the output array
    ndx=0
    # traverse though the counter list
    for i in range(len(counter)):
        # if the count of i is more than 0, then append that many 'i'
        while 0<counter[i]:
            # rewrite the array which was given to make it ordered
            weights[ndx] = i
            ndx += 1
            # reset the counter back to the set of zero's
            counter[i] -= 1

# now we have a optimal sorting function in hand, lets sort the list of edges.
# a dictionary with weights of an edge and the vertexes involved in that edge.
vrwght={}
# take every vertex in the graph
for ver1 in the_graph:
    # take every vertex ver1 is connected to = ver2
    for ver2 in ver1.getConnections():
        # make the dictionary with the weights and the 2 vertex's involved with the edge (thier key)
        vrwght[ver1.connectedTo[ver2]]=[ver1.getId(),ver2.getId()]

print "\nThe edges with thier unsorted weights are"
print vrwght

temp_weights=vrwght.keys()
counting_sort(temp_weights,max_weight)

sorted_weights={}
for weight in temp_weights:
    sorted_weights[weight]=vrwght[weight]

print "\nAfter sorting"
print sorted_weights


# Now step 2 : now we the smallest edge wrt to weight and add it to the MST,
# IF the two nodes associated with the edge belong TO DIFFERENT sets.
# What? well see kruskal's algo for finding the MST is simple,
# we take the graph, remove all the edges and order them based on thier weight
# now we replace all the removed edges back to the "graph" (which we just now plucked clean)
# smallest first. Subject to the condition that adding a edge doesnt cause a CYCLE or LOOP
# to develop, a tree cant have such loops we must avoid them.so we skip them
# so this series of steps explains Kruskal's algorithm:
"""
1. Take all edges in an array and Sort that array (in an ascending order)
2. Take the next (minimum edge), examine its end nodes:
    a) If they belong to different sets, merge their sets and add that edge to the tree
    b) Otherwise skip the edge
3. Print the tree obtained.
"""

# 2. a) is the method used to check if adding a particular edge will cause a cycle,
# Thus comes the UNION-FIND algorithm :
# Many thanks to  David Eppstein of the University of California,
# this is taken from PADS, a library of Python Algorithms and Data Structures
class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

FIND
    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

UNION
    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        # if the object is not present in the dictionary make the object itself its own parent and set its weight as 1
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

MST={}
# lets make a union-find instance - this calls init 
X=UnionFind()

# sets up the graph - make singleton sets for each vertex
for vertex_key in the_graph.getVertices():
    # get all the vertices set up, make them parents of themselfs, each in thier individual sets
    # execute FIND for all the vertex's in the_graph
    X[the_graph.getVertex(vertex_key)]

# now the UNION.
for weight in sorted_weights:
    # here sorted_weights[weight] gives the set of 2 vertex's involved in the that edge
    if(X[the_graph.getVertex(sorted_weights[weight][0])]==X[the_graph.getVertex(sorted_weights[weight][1])]):
        # if both vertices have the same parent (name) then they are in the same set, so ignore this edge
        pass
    else:
        # else as they belong to different sets we can ADD this edge to the MST (MST will be a subset of sorted_weights)
        MST[weight]=sorted_weights[weight]
        # and merge the sets these two vertices belong to thus we call union on them.
        X.union(the_graph.getVertex(sorted_weights[weight][0]),the_graph.getVertex(sorted_weights[weight][1]))

# thus we have the MST done

print " \n\nIn the graph with these vertex's"
print the_graph.getVertices()

print "\n With these edges between the vertexes given above, we obtain a Minimal Spanning Tree\n"
print MST

print "\n Please note this is a dictionary with  key as the weight of the edge and value as the key's of the two vertex's involved in this edge"
        
        
    
    
    






    
        
