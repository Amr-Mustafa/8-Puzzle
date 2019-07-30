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
        frontier.put((root.priority[0], root.priority[1], root))

        # Prevent infinite loops.
        explored = set()

        while not frontier.empty():
            # Get the node with the best A* score from the frontier.
            current = frontier.get()[2]
            explored.add(current)

            # The search reached the goal node.
            if Problem.goal_test(current):
                goal = current

                # Get the path taken to the goal.
                path = []
                while current.state != root.state:
                    path.append(current.state)
                    current = current.parent
                path.append(root.state)
                path.reverse()

                print(path)
                print("Path Cost: " + str(goal.path_cost))
                print(explored)
                print("Search depth: " + str(goal.path_cost))

                return True

            # Explore the node by inserting all of its children
            # into the frontier.
            children = current.children()
            print(children)
            print(frontier)
            for child in children:
                if child not in explored and child not in frontier.queue:
                    #print(str(child.priority[0]) + " " + str(child.priority[1]))
                    frontier.put((child.priority[0], child.priority[1], child))

        return False
