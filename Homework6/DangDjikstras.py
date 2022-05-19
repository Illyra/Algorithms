"""
The goal of this program is to create a djikstra's algorithm  to understand how to implemeent it with a graph according to
chapter 17's example when doing the assignment. We would need to get the 4 cases of no edge relaxation, unvisited edges, and display the final
results of our data when creating it. 


"""
import heapq
import sys


#referenced https://www.youtube.com/watch?v=Ub4-nG09PFw
#referenced https://github.com/mburst/dijkstras-algorithm/blob/master/dijkstras.py
#referenced https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_Vertex(self, name, edges):
        self.vertices[name] = edges
    
    def STP(self, start, end):
        distance = {} #distance from the start of the nodes
        trackPrevious = {} #previous node
        trackVisit = {}
        trackPath = [] #the node that ques the nodes in the graph

        for vertex in self.vertices:
            if vertex == start: #setting the root
                distance[vertex] = 0
                heapq.heappush(trackPath, [0, vertex])
            else:
                distance[vertex] = sys.maxsize
                heapq.heappush(trackPath, [sys.maxsize, vertex])
            trackPrevious[vertex] = None
        
        while trackPath:
            shortPath = heapq.heappop(trackPath)[1] #finds the smallest distances
            if shortPath == end: #compares the two nodes if they are equal to one another we would go through that path
                path = []
                while trackPrevious[shortPath]: #traverses through the nodes until reaching the value of 0 at the root node which is the value of 0
                    path.insert(0, shortPath)
                    shortPath = trackPrevious[shortPath]
                path.insert(0, shortPath)
                print("The optimal path taken is: ")
                return path
            if distance[shortPath] == sys.maxsize: #all remaining vertices would be inaccessible from the source
                break

            print("Node("+shortPath+") is added to the visited. Weight:", {distance[shortPath]})

            for adjacentNode in self.vertices[shortPath]: #would look at all the nodes that are attched to the vertex
                Index = distance[shortPath] + self.vertices[shortPath][adjacentNode]
                if Index > distance[adjacentNode]: #shortest path to update the priority queue(relax)
                    print(f"No edge relaxation is needed for edge, {adjacentNode}")
                elif Index != distance[shortPath] + self.vertices[shortPath][adjacentNode]:
                    print("No unvisted outgoing edges from this node: ", adjacentNode)
                else:
                    distance[adjacentNode] = Index
                    trackPrevious[adjacentNode] = shortPath
                    trackVisit[adjacentNode] = shortPath
                    print("Relaxed: vertex["+adjacentNode+"]: OLD:", distance[adjacentNode], ", NEW: ", Index, "Paths: ", trackVisit)

                    for i in trackPath:
                        if i[1] == adjacentNode:
                            i[0] = Index 
                    heapq.heapify(trackPath)
        return distance
    
    def __str__(self):
        return str(self.vertices)



g = Graph()
g.add_Vertex('A', {'B': 4, 'C': 2})
g.add_Vertex('B', {'C': 3, 'D': 2, 'E': 3})
g.add_Vertex('C', {'B': 1, 'D': 4, 'E': 5})
g.add_Vertex('D', {})
g.add_Vertex('E', {'D': 1})
print(g.STP('A', 'F'))


