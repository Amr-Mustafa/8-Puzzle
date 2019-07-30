from queue import PriorityQueue
from Node import *


class Search:

    # A* search algorithm organizes the frontier as a
    # priority queue ordered using the cost function
    # f(n) = g(n) + h(n) where g(n) is the "backward"
    # cost and h(n) is the "forward" cost.
    @staticmethod
    def a_star():

        root = Node(Problem.initial_state)

        # The frontier keeps track of all candidate nodes
        # to be explored next.
        frontier = PriorityQueue()
        frontier.put((root.priority, root))

        # Prevent infinite loops.
        explored = set()

        while not frontier.empty():
            # Get the node with the best A* score from the frontier.
            current = frontier.get()[1]
            explored.add(current)

            # The search reached the goal node.
            if Problem.goal_test(current):
                path = []
                while current.state != root.state:
                    path.append(current.state)
                    current = current.parent
                path.append(root.state)
                for state in path:
                    print_board(state)
                return True

            # Explore the node by inserting all of its children
            # into the frontier.
            children = current.children()
            for child in children:
                if child not in explored or child not in frontier:
                    frontier.put((child.priority, child))

        return False
