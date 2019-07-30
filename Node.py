from Problem import Problem
from Helper import *


class Node:

    # Each node contains six components:
    # 1. State: the state in the state space to which the node corresponds;
    # 2. Parent: the node in the search tree that generated this node;
    # 3. Action: the action that was applied to the parent to generate this node;
    # 4. Path-Cost: the cost, g(n), of the path from the initial state to the node.
    # 5. Heuristic-Cost: the approximated cost, h(n), of the path from the node
    #    to another node associated with a goal state.
    # 6. A*-Score: f(n) = g(n) + h(n).
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action

        self.path_cost = path_cost
        self.heuristic_cost = Problem.manhattan_distance(self) if Problem.heuristic == "Manhattan-Distance" \
            else Problem.euclidean_distance(self)
        self.a_star_score = self.path_cost + self.heuristic_cost
        self.priority = (self.a_star_score, Problem.priority[action])

    # The function child_node takes the current node and an action and
    # returns the resulting child node. Note that the cost of moving
    # from one state of the game to another state is the same and
    # is equal to one.
    def child_node(self, action):
        new_state = Problem.transition(self, action)
        return Node(new_state, self, action, self.path_cost + 1)

    # The function children returns all possible children of the current node.
    def children(self):
        children = [
            Node.child_node(self, "Up"),
            Node.child_node(self, "Down"),
            Node.child_node(self, "Right"),
            Node.child_node(self, "Left")
        ]
        children = list(filter(lambda child: not same_state(child.state, self.state), children))
        return children
