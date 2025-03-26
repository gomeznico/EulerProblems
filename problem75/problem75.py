"""
Problem 75

It turns out that pu{12 cm} is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12cm: (3,4,5)
24cm: (6,8,10)
30cm: (5,12,13)
36cm: (9,12,15)
40cm: (8,15,17)
48cm: (12,16,20)

In contrast, some lengths of wire, like 20cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120cm it is possible to form exactly three different integer sided right angle triangles.

120cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?
"""
import math
import time
from collections import defaultdict
## Brute Force
# find all combos of a,b,c that are valid int right triangles
# keep count by having a set for ALL sums, and then seperate set for ones of multiple lengths
# O(n2) with 2 for loops

## Brute Force V2
# generate all integer squares
# for each c2, use sliding window to find squares (a2, b2) less than c2 that add to c2
# also O(n2), since still searching the the whole array less than n, n different times

## Generate Pyth Triples using Tree of Primitive Pyth. triples
# https://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
# multiply matirx with a col vector of a pyth triple to get a new pyth triple primitive
# ex: 3,4,5 with matrix A-> A*(a,b,c)

def Matrix_multiply(matrix,pyth_triple):
    def mult(row1,row2):
        return sum(a*b for a,b in zip(row1,row2))

    a = mult(matrix[0],pyth_triple)
    b = mult(matrix[1],pyth_triple)
    c = mult(matrix[2],pyth_triple)
    return (a,b,c)

# generate all Pyth Primitive triples that sum below limit
def all_pyth_primitives_below(limit):
    A = [[1,-2,2],
        [2,-1,2],
        [2,-2,3]]
    B = [[1,2,2],
        [2,1,2],
        [2,2,3]]
    C = [[-1,2,2],
        [-2,1,2],
        [-2,2,3]]
    matrices = [A,B,C]

    #  use BFS to traverse tree.  each node has 3 children
    out = [(3,4,5)]
    queue = [(3,4,5)]
    while queue:
        next_queue = []
        for triple in queue:
            for M in matrices:
                new_triple = Matrix_multiply(M, triple)
                if sum(new_triple)<=limit:
                    next_queue.append(new_triple)
                    out.append(new_triple)
        queue = next_queue
    return out


limit = 1_500_000
pyth_primitives= all_pyth_primitives_below(limit)
print(len(pyth_primitives))

arrangements = defaultdict(int)
for pyth in pyth_primitives:
    length = sum(pyth)
    for i in range(1,(limit//length)+1):
        arrangements[length*i] +=1

counts = [n for n in arrangements.keys() if arrangements[n]==1 and n<=limit]
print(len(counts))
