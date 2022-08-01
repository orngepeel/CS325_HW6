# Author: Devon Braner
# GitHub Username: orngepeel
# Date: 7/31/2022
# Description: Implementation of Prim's algorithm for calculating minimum spanning tree.
# Citations: Code based off of pseudocode provided in modules
# Pseudocode involving min-heap from code practice solution:
# https://canvas.oregonstate.edu/courses/1878197/pages/exploration-minimum-spanning-tree-prims-algorithm?module_item_id=22307147
# Code involving min-heap implementation from Dijkstra's algorithm code practice solution:
# https://canvas.oregonstate.edu/courses/1878197/pages/exploration-dijkstras-algorithm?module_item_id=22307139

import heapq

def Prims(G):
    """
    Takes a graph represented as an adjacency matrix and calculates the minimum spanning tree of that graph.

    :param G: An adjacency matrix representing the input graph.

    :return: A list of tuples representing the edges of the minimum spanning tree of the graph as (v1, v2, weight).
    """
    # Arbitrary large number in place of infinity
    INF = 999999

    # Initialize a list to store object versions of the nodes in our graph
    nodes = []

    # Initialize the nodes
    for i in range(len(G)):
        nodes.append({'index': i,   # index for easy access to each node
                      'neighbors': [],
                      'parent': None,
                      'distance': INF,  # initialize distance to our arbitrary large number, update with minimum later
                      'visited': False})    # Track if visited on node to easily skip processing if needed.

    # Populate the neighbor lists
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j] > 0:
                nodes[i]['neighbors'].append(j)

    # Select a source node
    source = nodes[0]

    # Initialize a min-heap that will use distances to choose which node to process next
    # holds edge weights in a tuple using the format (weight, index)
    distances = []
    # List to track visits for the while loop.
    visited = [False] * len(G)

    # Initialize list to store results.
    result = []

    # Add our source to the heap, we will start here. the source is its own parent
    distances.append((0, source['index']))
    source['parent'] = source['index']

    # Traverse the graph until we have visited all nodes
    while False in visited:
        # unpack tuple from min-heap
        current_distance, current_node = heapq.heappop(distances)
        # Only process nodes we haven't visited already
        if nodes[current_node]['visited']:
            continue
        # We don't need the source node as a destination in our results... that would just be (0, 0, 0)
        if current_node != 0:
            result.append((nodes[current_node]['parent'], nodes[current_node]['index'], current_distance))

        # Access the current node's neighbors
        current_neighbors = nodes[current_node]['neighbors']
        # iterate through the neighbors
        for i in range(len(current_neighbors)):
            # See if the distance needs to be updated
            if min(G[current_node][current_neighbors[i]], nodes[current_neighbors[i]]['distance']) == G[current_node][current_neighbors[i]]:
                # Update distance and parent
                nodes[current_neighbors[i]]['distance'] = G[current_node][current_neighbors[i]]
                nodes[current_neighbors[i]]['parent'] = nodes[current_node]['index']
                # Push the (weight, index) to our min-heap
                heapq.heappush(distances, (nodes[current_neighbors[i]]['distance'], nodes[current_neighbors[i]]['index']))
        # Update current node visited status, and update visited index for our while loop.
        nodes[current_node]['visited'] = True
        visited[nodes[current_node]['index']] = True

    return result


if __name__ == '__main__':

    input1 = [
     [0, 8, 5, 0, 0, 0, 0],
     [8, 0, 10, 2, 18, 0, 0],
     [5, 10, 0, 3, 0, 16, 0],
     [0, 2, 3, 0, 12, 30, 14],
     [0, 18, 0, 12, 0, 0, 4],
     [0, 0, 16, 30, 0, 0, 26],
     [0, 0, 0, 14, 4, 26, 0]
    ]

    input = [
        [0, 8, 5, 0],
        [8, 0, 10, 2],
        [5, 10, 0, 3],
        [0, 2, 3, 0]
    ]
    print(Prims(input))
