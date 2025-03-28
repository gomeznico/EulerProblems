"""
Problem 86

A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner. By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.
It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100. This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.
Find the least value of M such that the number of solutions first exceeds one million.
"""
import math, time
### Brute Force:
#  iterate trhough all valid triples, get sh path and check if integer



def shortest_path_is_int(a,b,c,perfect_squares:set):
    # a<=b<=c
    # path 1 = rect(CA) + rect(BA)
    # path 2 = rect(CA) + rect(CB)
    # path 3 = rect(CB) + rect(BA)

    # path1 => sqrt(  (a+b)^2 + (c)^2  ) FOIL => a2 + b2 + 2ab + c2
    # path2 => sqrt(  (a+c)^2 + (b)^2  )      => a2 + c2 + 2ac + b2
    # path3 => sqrt(  (c+b)^2 + (a)^2  )      => c2 + b2 + 2cb + a2

    # diff btwn paths is 2ab, 2ac, 2bc, since a2, b2, c2 are in all 3 equations
    # since a<=b<=c, shortest path will be min of a*b, a*c, b*c
    # shortest path of all 3 will be path1 , (a+b), c

    path1_sqrd = (c+b)*(c+b) + (a*a)
    path2_sqrd = (a+b)*(a+b) + (c*c)
    path3_sqrd = (c+a)*(c+a) + (b*b)
    min_sqd_path = min(path1_sqrd,path2_sqrd,path3_sqrd)

    ## increase pefect squares for checking
    max_sq = max(perfect_squares)
    n = math.sqrt(max_sq)+1
    while max(perfect_squares)<min_sqd_path:
        perfect_squares.add(n*n)
        n+=1
    return min_sqd_path in perfect_squares

def count_sp_ints(M):
    # O(n3) time - 3 for loops
    # @ M = 100, count = 2060, 1.27 sec
    # @ M = 200, count = 9034, 21.53 sec (20x lopnger for 2x)
    # @ M = 400, count =

    # max poss square = m^2 + (m+m)^2
    s = time.time()
    max_n = int(math.sqrt(M*M + 4*M*M))+1
    perfect_squares = set()
    for i in range(1,max_n):
        perfect_squares.add(i*i)
    limit = M+1
    count = 0
    arr = []
    for a in range(1,limit):
        for b in range(a,limit):
            for c in range(b,limit):
                if shortest_path_is_int(a,b,c,perfect_squares):
                    count+=1
                    trip = (a,b,c)
                    arr.append(trip)
    e = time.time()
    print(f"for max side length of {M}, {count} int shortest paths found in {e-s:f} seconds")
    print(arr)



## Method 2:
# use func from problem75 to generate pythgorean triples, and
# then 'generate' valid sizes a,b,c
"""
# any int shortest path is the hyp. of a pythogrean triple
# a,b,c => 3paths are hyp of triangles with legs:
# path 1: a+b , c
# path 2: a+c , b
# path 3: a, b+c

# path1 => sqrt(  (a+b)^2 + (c)^2  ) FOIL => a^2 + b62 + 2ab + c^2
# path2 => sqrt(  (a+c)^2 + (b)^2  )      => a^2 + c^2 + 2ac + b^2
# path3 => sqrt(  (c+b)^2 + (a)^2  )      => c^2 + b^2 + 2cb + a^2

# diff btwn paths is 2ab, 2ac, 2bc, since a^2 b^2, c^2 are in all 3 equations
# since a<=b<=c, shortest path will be min of a*b, a*c, b*c
# shortest path of all 3 will be path1 , with legs (a+b), c

## Check each pyth triple for cuboids that have that as shortest path
## ex: 3,4,5 => a=b and c are 3 and 4 where a<=b<=c

# if a+b = 3  and c = 4=>
#       1,2 and 4
# if a+b = 4  and c = 3=>
#   1,3 and 3
#   2,2 and 3

## ex: 6,8,10 (multiple of above pyth.)
# if a+b=6 and c=8:
#   1,5 and 8
#   2,4 and 8
#   3,3 and 8
# if a+b=8 and c=6:
#   1,7 and 6 invalid
#   2,6 and 6
#   3,5 and 6
#   4,4 and 6

# Note that sol'ns for 6,8,3 are not just multiples of 3,4,5
# it is necessary to genraete all pyth triples with side legs of <= limit M

"""

def all_pyth_primitives(limit):
    # time complexity:
    #   matrix multiply is O(1)
    #   total time is ~number of nodes ~= 3^depth of tree
    #   minimum leg in pyth triples is resulting from matrix A
    #   (3,4,5)->(5,12,13)->(7,x,x)->(9,x,x)...
    #   avg leg length at each level:
    #   3.5-> 13.5-> 52.83-> 206.83-> 809.7-> 3169-> 12,409
    #   leglength ~= 4^d
    #   reach limit @ 4^d, depth ~=log4(limit)
    #   num nodes = 3^d = 3^log4(limit) = limit^log4(3) = limit^(0.8)
    #   slightly less than linear, more than sqrt
    # total time complexity:
    # O(1)*O(limit)


    ## generate pyth. primitive triple with side lengths <= limit
    def Matrix_multiply(matrix,pyth_triple):
        # O(1) time complexity
        def mult(row1,row2):
            return sum(a*b for a,b in zip(row1,row2))

        a = mult(matrix[0],pyth_triple)
        b = mult(matrix[1],pyth_triple)
        c = mult(matrix[2],pyth_triple)
        return (a,b,c)

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
    d =0
    while queue:
        next_queue = []
        for triple in queue:
            for M in matrices:
                new_triple = Matrix_multiply(M, triple)
                a,b,c = new_triple
                # a not necessarily <=b
                if a<=limit or b<=limit:
                    next_queue.append(new_triple)
                    new_triple = tuple(sorted(new_triple))
                    out.append(new_triple)
        queue = next_queue
    return out

def all_pyth_triples(limit):
    # time complexity
    # O(limit/a) * (primitives)
    # avg a is limit//2, assuming a is spread evenly between 0->limit
    # O( limit / limit/2 )* (limit^1.2)
    # final complexity is O(limit^1.2) time


    # take all primitives, and create multiples
    primitives = all_pyth_primitives(limit) # O(limit^1.2)
    # number of primitives proportional to slightly more than linear to the limit
    out = primitives[::]
    for a,b,c in primitives:    # O(primitives)
        for n in range(2,(limit//a) + 1):  #O(limit/a)
            trip = (n*a, n*b, n*c)
            out.append(trip)
    return out

def valid_cuboids_of_triple(triple,limit):
    # O(1) time - num calculations is constant for each triple
    s1,s2,s3 = triple



    count = 0
    # s1 = a+b , s2 = c
    a,b,c = 1, s1-1 , s2
    # (1, ,c)
    # (2, ,c)
    #  ...
    ## total possible pairs of a,b where a<=b
    if c<= limit:
        pairs = (b+1)//2
        ## remove any pairs where b > c.
        ## need to account for issues where b might be so much larger, it removes too many pairs
        # i.e. pyth triple 1,24,25
        # if c == 1, a+b = 24.  no possible triples of a,b,c are valid
        # pairs of a,b = 12, but b-c = 23-1 = 22.
        # do not remove 'too many' pairs from count
        if b>c:
            remove = (b-c)
            pairs = max(pairs-remove, 0)
        count += pairs

    a,b,c = 1, s2-1, s1
    if c<= limit:
        pairs = (b+1)//2
        ## remove any where b > c
        if b>c:
            remove = (b-c)
            pairs = max(pairs-remove, 0)
        count += pairs

    return count

    """ old func for getting actual a b c dimenions:
    out = []
    # a+b = s1 and c=s2
    a,b,c = 1, s1-1 , s2
    while a<=b and c<=limit:
        if a<=b<=c:
            trip = (a,b,c)
            out.append(trip)
        a+=1
        b+= -1

    # a+b = s2 and c=s1
    a,b,c = 1, s2-1, s1
    while a<=b and c<=limit:
        if a<=b<=c:
            trip = (a,b,c)
            out.append(trip)
        a+=1
        b+= -1
    return out
    """

def int_solns_up_to(limit, timer = False):
    # O(triples)*O(1) time - triples is ~limit^1.2
    # final time complexity: O(limit^1.2)

    # 2060 , for M<= 100 in 0.1218 micro-seconds
    # 9034 , for M<= 200 in 0.3011 micro-seconds  (2x size -> ~2x time)
    # 40432 , for M<= 400 in 0.9489 micro-seconds (2x size -> ~3x time)
    # 281334 , for M<= 1000 in 3.886 micro-seconds

    #generate all pyth triples with legs <= limit
    pyth_triples = all_pyth_triples(limit)
    s = time.time()

    count = 0
    for triple in pyth_triples: # O(triples)
        count += valid_cuboids_of_triple(triple,limit) # O(1)
    e = time.time()
    if timer is True:
        print(f'{count} valid cuboids found with lengths <= {limit} in {1000*(e-s):.4} micro-seconds')
    return count

def solve(threshold):

    M = 1
    num_solns = int_solns_up_to(M)
    s = time.time()
    while num_solns < threshold:
        M+=1
        num_solns = int_solns_up_to(M)
        if M%100 == 0: print(f'checking {M}')
    e = time.time()
    print(f"cuboids up to side length {M} have {num_solns} integer shortest paths.  {e-s:.4} seconds ")


# solve(1_000)
# solve(10_000)
# solve(100_000)
solve(1_000_000)
# solve(10_000_000)
# cuboids up to side length 72 have 1057 integer shortest paths.  0.01588 seconds
# cuboids up to side length 210 have 10153 integer shortest paths.  0.172 seconds
# cuboids up to side length 616 have 100953 integer shortest paths.  1.855 seconds
# cuboids up to side length 1818 have 1000457 integer shortest paths.  20.311 seconds
# cuboids up to side length 5400 have 10015662 integer shortest paths.  206.5 seconds

