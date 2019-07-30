# Check if two states of the game are equal.
def same_state(s1, s2):
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


# Textual representation of the given state.
def print_board(state):
    print(" --- --- ---")
    print("| " + state[0] + " | " + state[1] + " | " + state[2] + " |")
    print(" --- --- ---")
    print("| " + state[3] + " | " + state[4] + " | " + state[5] + " |")
    print(" --- --- ---")
    print("| " + state[6] + " | " + state[7] + " | " + state[8] + " |")
    print(" --- --- ---")
    print("      ^")
    print("      |")
    print("      |")
