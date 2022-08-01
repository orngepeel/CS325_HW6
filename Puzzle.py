# Author: Devon Braner
# GitHub Username: orngepeel
# Date: 7/31/2022
# Description: Uses BFS to solve a 2-D puzzle of size MxN, where the goal is to find the shortest path from the source
#               to the destination.
# Citations:

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

    source_row, source_column = source
    destination_row, destination_column = destination
    row_queue = []
    column_queue = []
    row_directions = [-1, 1, 0, 0]
    column_directions = [0, 0, 1, -1]

    steps_taken = 0
    remaining_layer = 1
    next_layer = 0

    destination_reached = False

    visited = [[False] * len(board)] * len(board[0])

    row_queue.append(source_row)
    column_queue.append(source_column)

    visited[source_row][source_column] = True

    while len(row_queue) > 0:
        current_row = row_queue.pop(0)
        current_column = column_queue.pop(0)

        if (current_row, current_column) == (destination_row, destination_column):
            destination_reached = True
            break

        for i in range(0, len(row_directions)):
            potential_row_neighbor = current_row + row_directions[i]
            potential_column_neighbor = current_column + column_directions[i]

            if potential_row_neighbor < 0 or potential_column_neighbor < 0:
                continue
            if potential_row_neighbor >= len(board) or potential_column_neighbor >= len(board[0]):
                continue

            if visited[potential_row_neighbor][potential_column_neighbor]:
                continue
            if board[potential_row_neighbor][potential_column_neighbor] == '#':
                continue

            row_queue.append(potential_row_neighbor)
            column_queue.append(potential_column_neighbor)
            visited[potential_row_neighbor][potential_column_neighbor] = True
            next_layer += 1

        remaining_layer -= 1
        if remaining_layer == 0:
            remaining_layer = next_layer
            next_layer = 0
            steps_taken += 1

    return steps_taken


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