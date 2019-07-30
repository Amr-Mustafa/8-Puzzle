import copy


class Problem:

    # Global problem settings.
    heuristic = "Manhattan-Distance"
    initial_state = [
        '8', '7', '6',
        '5', '4', '3',
        '2', '1', '0'
    ]
    goal_state = [
        '0', '1', '2',
        '3', '4', '5',
        '6', '7', '8'
    ]

    # Tie breaking.
    priority = {
        'Up': 3,
        'Down': 4,
        'Right': 1,
        'Left': 2,
        None: 0
    }

    # The goal_coordinates list specifies the final position
    # of each cell in the puzzle.
    goal_coordinates = {
        '0': (0, 0),  # Final position of the blank cell.
        '1': (0, 1),  # Final position of cell '1'.
        '2': (0, 2),  # Final position of cell '2'.
        '3': (1, 0),  # and so on.
        '4': (1, 1),
        '5': (1, 2),
        '6': (2, 0),
        '7': (2, 1),
        '8': (2, 2)
    }

    # The transition function returns the state that results
    # from doing the given action in the state corresponding
    # to the given node. Note that the possible actions are
    # swapping the blank tile with a component in one of the
    # four directions: 'Up', 'Down', 'Left', 'Right'.
    @staticmethod
    def transition(node, action):
        current_state = copy.deepcopy(node.state)
        blank_tile_position = current_state.index('0')

        # A blank tile on the first row can't be moved up.
        if action == 'Up' and blank_tile_position > 2:
            temp = current_state[blank_tile_position - 3]
            current_state[blank_tile_position - 3] = '0'
            current_state[blank_tile_position] = temp

        # A blank tile on the third row can't be moved down.
        elif action == 'Down' and blank_tile_position < 6:
            temp = current_state[blank_tile_position + 3]
            current_state[blank_tile_position + 3] = '0'
            current_state[blank_tile_position] = temp

        # A blank tile on the third column can't be moved right.
        elif action == 'Right' and (blank_tile_position + 1) % 3 != 0:
            temp = current_state[blank_tile_position + 1]
            current_state[blank_tile_position + 1] = '0'
            current_state[blank_tile_position] = temp

        # A blank tile on the first column can't be moved left.
        elif action == 'Left' and blank_tile_position % 3 != 0:
            temp = current_state[blank_tile_position - 1]
            current_state[blank_tile_position - 1] = '0'
            current_state[blank_tile_position] = temp

        return current_state

    # The goal test determines whether a given state is a goal state.
    @staticmethod
    def goal_test(node):
        return node.state == Problem.goal_state

    # Heuristic 1: The manhattan distance is the sum of absolute values
    # of differences in the goal's x and y coordinates and the current
    # cell's x and y coordinates respectively.
    @staticmethod
    def manhattan_distance(node):

        state = node.state
        total_distance = 0

        # We will calculate the manhattan distance between every cell
        # in the current state and the its appropriate position in the
        # goal state. The sum of each manhattan distance is the result.
        for cell in state:
            cell_index = state.index(cell)
            cell_coordinates = (0 if cell_index < 3 else 1 if cell_index < 6 else 2, cell_index % 3)
            goal_coordinates = Problem.goal_coordinates[cell]
            total_distance += abs(cell_coordinates[0] - goal_coordinates[0]) + \
                abs(cell_coordinates[1] - goal_coordinates[1])
        return total_distance

    # Heuristic 2: The euclidean distance between the current cell
    # and the goal cell using the distance formula.
    @staticmethod
    def euclidean_distance(node):

        state = node.state
        total_distance = 0

        # We will calculate the euclidean distance between every cell
        # in the current state and the its appropriate position in the
        # goal state. The sum of each euclidean distance is the result.
        for cell in state:
            cell_index = state.index(cell)
            cell_coordinates = (0 if cell_index < 3 else 1 if cell_index < 6 else 2, cell_index % 3)
            goal_coordinates = Problem.goal_coordinates[cell]
            total_distance += ((cell_coordinates[0] - goal_coordinates[0]) ** 2 +
                               (cell_coordinates[1] - goal_coordinates[1]) ** 2) ** 0.5
        return total_distance
