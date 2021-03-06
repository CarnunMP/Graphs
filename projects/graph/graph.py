"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue firt vertex
        to_visit = Queue()
        to_visit.enqueue(starting_vertex)
        # create a set to store visited vertices
        visited = set()

        # loop over queue until empty
        while to_visit.size() > 0:
            # dequeue first vertex
            current_vertex = to_visit.dequeue()

            # if it hasn't been visited
            if current_vertex not in visited:
                # mark as visited and print
                visited.add(current_vertex)
                print(current_vertex)

                # iterate over its children
                for child_vertex in self.vertices[current_vertex]:
                    # enqueue them
                    to_visit.enqueue(child_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Same as above, but using a stack...!
        to_visit = Stack()
        to_visit.push(starting_vertex)

        visited = set()

        while to_visit.size() > 0:
            current_vertex = to_visit.pop()

            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)

                for child_vertex in self.vertices[current_vertex]:
                    to_visit.push(child_vertex)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # base case: no children, print
        # recursive case: print, and call dft_recursive on each unvisited child

        # So, printing happens each time regardless:
        print(starting_vertex)
        visited.add(starting_vertex)

        if len(self.vertices[starting_vertex]) > 0:
            for child_vertex in self.vertices[starting_vertex]:
                if child_vertex not in visited:
                    self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Same as bft, except we're keeping track of the path taken
        # and stopping once we reach destination_vertex

        to_visit = Queue()
        to_visit.enqueue([starting_vertex]) # enqueuing a _path_, here

        visited = set()

        while to_visit.size() > 0:
            current_path = to_visit.dequeue()
            last_vertex = current_path[-1]

            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return current_path

                visited.add(last_vertex)
                for child_vertex in self.vertices[last_vertex]:
                    to_visit.enqueue(current_path + [child_vertex])


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # same as dft, except, again, we're keeping track of _paths_
        to_visit = Stack()
        to_visit.push([starting_vertex])

        visited = set()

        while to_visit.size() > 0:
            current_path = to_visit.pop()
            last_vertex = current_path[-1]

            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return current_path

                visited.add(last_vertex)
                for child_vertex in self.vertices[last_vertex]:
                    to_visit.push(current_path + [child_vertex])

    def dfs_recursive(self, starting_vertex, destination_vertex, current_path=[], visited=set()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # base case: current_vertex is destination_vertex OR no children
        # recursive case: otherwise

        current_path = current_path + [starting_vertex]
        visited.add(starting_vertex)
    
        if starting_vertex == destination_vertex:
            return current_path

        if len(self.vertices[starting_vertex]) > 0:
            for child_vertex in self.vertices[starting_vertex]:
                if child_vertex not in visited:
                    path = self.dfs_recursive(child_vertex, destination_vertex, current_path, visited)
                    if path is not None:
                        return path



if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
