"""traversal of Graph: Depth First Search (DFS)

   [application](https://www.geeksforgeeks.org/?p=11644):
   * for an unweighted graph, DFS traversal of the graph produces the minimum
     spanning tree and all pair shortest path tree.
   * Path finding
   * topologil sorting
   * to test if a graph is bipartite
   * finding strongly connected components
   * solving puzzles with only one solution

   complexity:
"""
from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v)

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        V = list(self.graph.keys())
        visited = dict(zip(
            V, [False] * len(V)))

        for i in V:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def BFS(self, s):
        V = list(self.graph.keys())
        visited = dict(zip(
            V, [False] * len(V)))

        frontier = []

        frontier.append(s)
        visited[s] = True

        while frontier:
            s = frontier.pop(0)
            print(s)

            for i in self.graph[s]:
                if visited[i] == False:
                    frontier.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("Following is BFS traversal (starting from vertex 2)")
    g.BFS(2)
