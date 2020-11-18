
"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges"""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # Check if v1 and v2 exists in vertices list
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 at v1 of vertices
            self.vertices[v1].add(v2)
        # Otherwise
        else:
            # Raise an error
            raise KeyError("That vertex does not exists")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create and empty queue and enqueue the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)

        # Create a set to store the visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # If that vertex has not been visited
            if v not in visited:
                # Mark it as visited printing printing for a representation
                print(v)
                visited.add(v)
                # then add all ofit's neighbor to the back of the queue
                for next_vertex in self.vertices[v]:
                    q.enqueue(next_vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack and push the taring vertex
        s = Stack()
        s.push(starting_vertex)

        # Create a set to store the visited vertices
        visited = set()

        # While the stack is not empty
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()

            # If that vertex has not been visited
            if v not in visited:
                # Mark it as visited printing for a representation
                print(v)
                visited.add(v)
                # Then add all of it's neighboursto the top of the stack
                for next_vertex in self.vertices[v]:
                    s.push(next_vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Set base case for when the visited is None and create an empty set
        if visited is None:
            visited = set()
        print(starting_vertex)
        visited.add(starting_vertex)
        #
        for child_vertex in self.vertices[starting_vertex]:
            # if the vertex is not in visited
            if child_vertex not in visited:
                # Call the recursive function
                self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create and empty queue and enqueue the starting vertex
        q = Queue()
        q.enqueue([starting_vertex])

        # Create a set to store the visited vertices
        visited = set()

        # While the queue is not empty
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]

            # Check if vertex has been visited:
            if vertex not in visited:
                # Check if it's the destination vertex
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                # Create new path
                for next_vertex in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create and empty stack and push the starting vertex
        stack = Stack()
        stack.push([starting_vertex])

        # Create a set to store the visited vertices
        visited = set()

        # While the stack is not empty
        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]

            # Check if vertex has been visited:
            if vertex not in visited:
                # Check if it's the destination vertex
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                # Create new path
                for next_vertex in self.vertices[vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, goal_vertex):
        visited = set()
        return self.dfs_recursive_helper([starting_vertex], visited, goal_vertex)

    def dfs_recursive_helper(self, curr_path, visited, goal_vertex):
        curr_vertex = curr_path[-1]
        if curr_vertex == goal_vertex:
            return curr_path
        visited.add(curr_vertex)
        for neighbor in self.vertices[curr_vertex]:
            if neighbor not in visited:
                newPath = list(curr_path)
                newPath.append(neighbor)
                res = self.dfs_recursive_helper(newPath, visited, goal_vertex)
                if len(res) > 0:
                    return res
        return []


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
