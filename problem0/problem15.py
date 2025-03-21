"""
in 2x2 grid, there are 6 paths to get from teh very top left to the very bottom right
can only move down and right. no loops

how many paths are there in a 20x20 grid?



2x2 grid is == to 3x3 grid of nodes to travel between
9 total nodes, -start and end nodes -> 7 nodes

do a DFS, and add to count when the end node is reached
do not keep track of visited nodes
 can only go right or down

 in 1x1, there are 2 lengths total, 2 paths
 in 2x2, there are 4 lengths req, 6 paths total
    right right, down down
    rights must equal downs
    how many ways are there to assemble 1 and -1 such that the sum = 0
in 20x20, there are 40 lengths req

"""



num_paths = 0
stack = []


