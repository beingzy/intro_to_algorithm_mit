"""Greedy Aglorithm: Dijkstra's Shortest Path Algorithm
   find the shortest path from A to B, suitable for
   DAG (directed acyclic graph) with non-negative weights

   author: Yi Zhang <beingzy@gmail.com>
   date: 2018/01/25
"""
import sys
import math


class Graph():
    """Dijkstra's single source shortest path algorithm. The program
       is for adjacency matrix representation of the graph
    """

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(len(vertices))]
                      for row in range(len(vertices))]

    def print_solution(self, dist):
        print('Vertex distance from source')
        for node in range(len(self.V)):
            print(node, 't', dist[node])

    def min_distance(self, dist, spt_set):
        """utility functon to find the vertex with minimum distance
           value, from the set of vertices not yet included in
           shortest path tree
        """
        # initilaize minimum distance for adjacent nodes
        _min = math.inf

        for v in range(len(self.V)):
            if dist[v] < _min and spt_set[v] == False:
                _min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        """function that implements Dijkstra's single source
           shortest path algorithm for a graph represented using
           adjacency matrix representation.
        """
        dist = [math.inf] * len(self.V)
        dist[src] = 0
        spt_set = [False] * len(self.V)

        for cout in range(len(self.V)):
            # pick the minimum disetance vertex from the
            # set of vertices not yet processed.
            # us is always equal to src in first iteration
            u = self.min_distance(dist, spt_set)

            # put the minimum disetance vertex in the shortest
            # path tree
            spt_set[u] = True

            # update dist vallue of the adjacent vertices of
            # the picked vertex only if the current distance
            # is greater than new ditance and the vertex in
            # not in the shortest path tree
            for v in range(len(self.V)):
                if self.graph[u][v] > 0 and spt_set[v] == False:
                    alt_dist = dist[u] + self.graph[u][v]
                    if dist[v] > alt_dist:
                        dist[v] = alt_dist

            self.print_solution(dist)


if __name__ == "__main__":
    g = Graph(list(range(9)))
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    g.dijkstra(0)
