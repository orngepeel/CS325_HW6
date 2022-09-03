# CS325_HW6
This was the portfolio assignment for CS 325 Analysis of Algorithms

### MST.py
An implementation of Prim's algorithm. Given an adjacency matrix, outputs a list of tuples that represents the minimum spanning tree of the graph.

### Puzzle.py
Given a 2-D puzzle of size MxN, that has N rows and M column (M and N can be different), two coordinates from the puzzle (a,b) and (x,y), and the ability to move in the following directions:
- L: move to left cell from the current cell 
- R: move to right cell from the current cell 
- U: move to upper cell from the current cell 
- D: move to the lower cell from the current cell
returns the path from (a,b) to (x,y).
Utilizes BFS to find the shortest path.
