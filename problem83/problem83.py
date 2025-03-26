"""
Problem 83

NOTE: This problem is a significantly more challenging version of Problem 81.
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by moving left, right, up, and down, is indicated in bold red and is equal to 2297.


begin{pmatrix}
131x , 673 , 234 , 103 , 18
201x , 96x , 342 , 965 , 150
630 , 803 , 746 , 422 , 111
537 , 699 , 497 , 121 , 956
805 , 732 , 524 , 37 , 331
end{pmatrix}


Find the minimal path sum from the top left to the bottom right by moving left, right, up, and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

import heapq
import time
from collections import defaultdict

input = open('problem81/matrix.txt','r').read()[0:-1]

test_input = """131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331"""

def parse(input):
    m = [[int(c) for c in line.split(',')] for line in input.split('\n')]
    return m

## use dijkstra starting from each left to any right col

def neighbors(coord,matrix):
    ## only move up, down, left, right
    limit = len(matrix)
    row,col = coord
    out = []
    d = [(-1,0), (+1,0), (0,+1), (0,-1)]
    for drow,dcol in d:
        if 0<= row+drow < limit and 0<= col+dcol < limit:
            c = (row+drow, col+dcol)
            out.append(c)
    return out

def val(coord,matrix):
    if coord == (-1,-1): return 0
    row,col = coord
    return matrix[row][col]

## method  Dijkstra:
def dijkstra(matrix, start, end=None):
    s = time.time()
    if end == None:
        limit = len(matrix)
        end = (limit-1,limit-1)

    node = (val(start,matrix), start)
    pq = [node]     # nodes are tuples of (dist, curr_coord)
    heapq.heapify(pq)

    shortest_dist = defaultdict(lambda :float('inf'))
    ## don't particularly care about path, only node coord and travel dist
    ## no need to save parent of each node to recreate shortest path
    while pq:
        curr_dist , coord = heapq.heappop(pq)

        #check dist
        if curr_dist > shortest_dist[coord]: continue


        ## add neighbors onto queue
        for next_coord in neighbors(coord,matrix):
            new_dist = curr_dist+val(next_coord,matrix)

            if new_dist<shortest_dist[next_coord]:
                shortest_dist[next_coord] = new_dist
                node = (new_dist, next_coord)
                heapq.heappush(pq, node)

        if coord == end:
            e = time.time()
            print(f'found shortest path to {coord} in {1000*(e-s):f} micro-seconds:  weight is {curr_dist} ')
            break



matrix = parse(input)
start = (0,0)
dijkstra(matrix,start)
# found shortest path to (79, 79) in 16.491652 micro-seconds:  weight is 425185 
