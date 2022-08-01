# Author: Devon Braner
# GitHub Username: orngepeel
# Date: 7/31/2022
# Description: Uses BFS to solve a 2-D puzzle of size MxN, where the goal is to find the shortest path from the source
#               to the destination.
# Citations:
# Strategy derived from these videos:
#       https://www.youtube.com/watch?v=e69C6xhiSQE&t=641s
#       https://www.youtube.com/watch?v=KiCBXu4P-2Y
#       https://www.youtube.com/watch?v=oDqjPvD54Ss
# Used some tips for tuples from here:
#       https://stackoverflow.com/questions/2191699/find-an-element-in-a-list-of-tuples

def solve_puzzle(board, source, destination):
    """
    Given a 2-D puzzle of size N rows and M columns, where empty cells are marked by '-', and cells that act as barriers
        are marked by '#'. Finds the shortest path from the source to the destination.

    :param board: List of lists. Each list represents a row of the puzzle. Elements are either '-' (empty) or
                    '#' (passable).
    :param source: Tuple. represents the indices of the starting position.
    :param destination: Tuple. Represents the indices of the goal position.

    :return: List of Tuples representing the indices of each position in the path.
    """
    # Unpack source tuple
    source_row, source_column = source
    # Initialize queue for BFS traversal
    coord_queue = []

    # Direction vectors
    row_directions = [-1, 1, 0, 0]
    column_directions = [0, 0, 1, -1]

    # Variables for tracking steps and layers of BFS
    steps_taken = 0
    remaining_layer = 1
    next_layer = 0

    # Variable to track when we have reached our destination
    destination_reached = False
    # Set to hold our visited cells
    visited = set()
    # Set to hold tuples of visited cells and the coordinates of the previous associated cell
    visited_path = set()

    # enqueue the source cell
    coord_queue.append((source_row, source_column))

    # Initialize a tuple to track previous cells
    previous_row, previous_column = None, None

    # Add the source to both visited sets
    visited.add((source_row, source_column))
    visited_path.add(((source_row, source_column), (previous_row, previous_column)))

    # Traverse through the puzzle
    while len(coord_queue) > 0:
        # Unpack current coordinates from the queue
        current_row, current_column = coord_queue.pop(0)
        # If we have reached the destination, stop traversal
        if destination == (current_row, current_column):
            destination_reached = True
            break

        # Find all neighboring cells using the direction vectors
        for i in range(0, 4):
            potential_row_neighbor = current_row + row_directions[i]
            potential_column_neighbor = current_column + column_directions[i]
            # Check that the potential neighbor meets the required conditions:
            # Does it go out of bounds?
            if potential_row_neighbor < 0 or potential_column_neighbor < 0:
                continue
            if potential_row_neighbor >= len(board) or potential_column_neighbor >= len(board[0]):
                continue
            # Have we already visited this cell?
            if (potential_row_neighbor, potential_column_neighbor) in visited:
                continue
            # Is this cell blocked?
            if board[potential_row_neighbor][potential_column_neighbor] == '#':
                continue
            # If the cell is legal, enqueue it.
            coord_queue.append((potential_row_neighbor, potential_column_neighbor))
            # Then update the previous cell
            previous_row, previous_column = current_row, current_column
            # add the cell to our visited sets so we don't check it again.
            visited.add((potential_row_neighbor, potential_column_neighbor))
            visited_path.add(((potential_row_neighbor, potential_column_neighbor), (previous_row, previous_column)))
            # increment tracker for how many cells we check in the next round of BFS
            next_layer += 1
        # At each loop decrement counter for current BFS layer
        remaining_layer -= 1
        # Once we process all the cells in the layer
        if remaining_layer == 0:
            # proceed to next layer
            remaining_layer = next_layer
            next_layer = 0
            # increment steps taken
            steps_taken += 1

    # Once we have reached the destination, we need to process the path taken
    if destination_reached is True:
        # Initialize a results list using the number of steps taken
        results_list = [None for i in range(steps_taken + 1)]
        # Turn our visited path into a dictionary for easy access
        visited_path = dict(visited_path)
        # Start at the destination
        results_list[0] = destination
        for i in range(1, steps_taken + 1):
            # Use the previous cell coordinates from the visited_path dictionary to traverse our final path backwards
            results_list[i] = visited_path[results_list[i-1]]
        # Reverse the list so it's in the correct order
        results_list.reverse()
        return results_list
    # If we could not reach the destination, we return None.
    else:
        return None

if __name__ == '__main__':
    Puzzle = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-'],
        ['-', '#', '-', '-', '-']
    ]
    print(solve_puzzle(Puzzle, (0,2), (2, 2)))
    print(solve_puzzle(Puzzle, (0, 0), (4, 4)))
    print(solve_puzzle(Puzzle, (0, 0), (4, 0)))