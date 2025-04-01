"""
Problem 94

It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.
We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.
Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""
import math, time
## Method 1 Brute Force:
# triangles area sides a,a,b
# iterate through all a from 1-> limit//3+1  ... limit is inclusive.
# ex. 1000, a=334, b can be 333, but not 335.

## Method 2 check against pyth triples:
# a,a,b -> area = .5 *b*h -> h2 + b2/4 = a2
# for integer perim, h, b/2, and a must be pyth tripl
# for int area     .5b*h must be int, which is true if pyth. tripl

# generate all pyth. triples:
# check if each can be an almost-eq triangle by checking hyp = 2*side +/- 1


def is_int_triangle_area(a,b):
    if (b*b)%4!=0: return False
    # area = 1/2 * b*h
    # (b/2)^2 + h^2 = a^2
    # h^2 = a^2 - b^2/4
    h2 = a*a - b*b//4

    h = int(math.sqrt(h2)) - 2
    while h*h<h2:
        h+=1
    return h*h == h2

def solve(limit):
    s = time.time()

    # perf = set()
    # for n in range(1,limit//3+1):
    #     perf.add(n*n)

    count = 0   # triangle 1,1,2 has no integer area, is invalid
    perim = 0
    for a in range(3,limit//3+2,2):
        # b must be even for 1/2 to be integer
        # so a must be odd
        for b in [a+1,a-1]:
            if is_int_triangle_area(a,b):
                count+=1
                perim += a+a+b
                print(a,a,b, f'total perim = {a+a+b}')

    e = time.time()
    print(f'{limit//3*2:_} triangles checked.  {count} found with integer area and perimeters')
    print(f'for a total perim {perim}. {e-s:f} seconds elapsed')

# generate all Pyth Primitive triples where hyp is below limit
def all_pyth_primitives_below(limit,display=False):

    def Matrix_multiply(matrix,pyth_triple):
        def mult(row1,row2):
            return sum(a*b for a,b in zip(row1,row2))

        a = mult(matrix[0],pyth_triple)
        b = mult(matrix[1],pyth_triple)
        c = mult(matrix[2],pyth_triple)
        return (a,b,c)


    matrices = [
        [[1,-2,2],
        [2,-1,2],
        [2,-2,3]],

        [[1,2,2],
        [2,1,2],
        [2,2,3]],

        [[-1,2,2],
        [-2,1,2],
        [-2,2,3]]]

    #  use BFS to traverse tree.  each node has 3 children
    out = [(3,4,5)]
    queue = [(3,4,5)]
    i = 0
    while queue:
        i+=1
        if i%5==0 and display: print(f'at depth {i} in pyth tree, out is size {len(out):_}, hyp length at {out[-1][2]:_}')
        next_queue = []
        for triple in queue:
            for M in matrices:
                new_triple = Matrix_multiply(M, triple)
                a,b,c = new_triple
                if c <= limit:
                    next_queue.append(new_triple)
                    out.append(new_triple)
        queue = next_queue
    return out

def solveV2(limit):

    s = time.time()
    # get all pyth where hyp is below max leg length
    pyth_triples = all_pyth_primitives_below(limit//3+1)
    ## get all multiples of pyth triples too
    print(f'generated {len(pyth_triples):_} pyth triples')
    valid = 0
    total_perim = 0
    i = 0
    for a,b,c in pyth_triples:
        i+=1
        if i%10_000_000 == 0: print(f'{i:_}')
        # hypotenuese = c
        # mirror in one dir
        if c == 2*b - 1 or c == 2*b + 1:
            #c,c,2*b
            valid+=1
            total_perim += c+c+(2*b)
            print(c,c,2*b)
        if c == 2*a - 1 or c == 2*a + 1:
            #c,c,2*a
            valid+=1
            total_perim += c+c+(2*a)
            print(c,c,2*b)
    e = time.time()
    # print(triangles)
    print(f'{len(pyth_triples)*2:_} triangles checked.  {valid} found with integer area and perimeters')
    print(f'for a total perim {total_perim}. {e-s:f} seconds elapsed')



limit = 1_000_000_000
solve(limit)
solveV2(limit)
# 666_666_666 triangles checked.  14 found with integer area and perimeters
# for a total perim 518_408_346. 167.190519 seconds elapsed


# pyth multiples-> takes very long time to generate triples...
# 106_103_396 triangles checked.  14 found with integer area and perimeters
# for a total perim 518408346. 289.439247 seconds elapsed

