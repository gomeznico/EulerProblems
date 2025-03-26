"""
Problem 81

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.

{131}  673    234  103  18
{201}  {96}  {342}  965  150
630    803  {746}  {422}  111
537    699   497  {121}  956
805    732   524  {37}  {331}

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""
import heapq
import time
from collections import defaultdict

# first line:
# 4445,2697,5115,718,2209,2212,654,4348,3079,6821,7668,3276,8874,4190,3785,2752,9473,7817,9137,496,7338,3434,7152,4355,4552,7917,7827,2460,2350,691,3514,5880,3145,7633,7199,3783,5066,7487,3285,1084,8985,760,872,8609,8051,1134,9536,5750,9716,9371,7619,5617,275,9721,2997,2698,1887,8825,6372,3014,2113,7122,7050,6775,5948,2758,1219,3539,348,7989,2735,9862,1263,8089,6401,9462,3168,2758,3748,5870
input = open('problem81/matrix.txt','r').read()[0:-1].split('\n')

# 80x80 matrix
matrix = []
for line in input:
    row = [ int(c) for c in line.split(',')]
    matrix.append(row)
test_matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630 , 803, 746, 422 , 111],
    [537 , 699, 497, 121, 956],
    [805, 732, 524, 37, 331]]

def neighbors(coord, matrix):
    ## only move right and dwn
    limit = len(matrix)
    row,col = coord
    out = []
    d = [(0,+1), (+1,0)]
    for drow,dcol in d:
        if 0<= row+drow < limit and 0<= col+dcol < limit:
            c = (row+drow, col+dcol)
            out.append(c)
    return out

def val(coord,matrix):
    row,col = coord
    return matrix[row][col]

## method 1 Brute Force:
# go through all possible paths go down 80 and over 80, 160 total moves 2^160!!!

## method 2 Dijkstra:
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

start = (0,0)
dijkstra(test_matrix,start)
# found shortest path to (4,4) in 0.048161 micro-seconds:  weight is 2427
dijkstra(matrix,start)
# found shortest path to (79, 79) in 11.016846 micro-seconds:  weight is 427337
