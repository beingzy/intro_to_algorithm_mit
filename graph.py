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

    def topological_sort_util(self, v, visited, stack):
        """recursive method for implementing topological sorting
        """
        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        """topological sorting [link](https://goo.gl/Levz6s)
        """
        V = list(self.graph.keys())
        visited = dict(zip(V, [False] * len(V)))
        stack = []

        for v in V:
            if visited[v] == False:
                self.topological_sort_util(v, visited, stack)

        print(stack)


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

    # test case for topological sorting
    g = Graph()
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    print("Following is a Topological Sort of the given graph")
    g.topological_sort()
