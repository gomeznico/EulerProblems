"""
Problem 91

The points P(x_1, y_1) and Q(x_2, y_2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form triangle OPQ.


There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is, 0<=x_1, y_1, x_2, y_2<=2.


Given that 0<=x_1, y_1, x_2, y_2<=50, how many right triangles can be formed?
"""
import math, time, itertools
## brute force:
# check all possible combos of coords
# triangle is made of 3 pts: Origin, A, B.  Origin is always (0,0)
# coord are all integer points.  all possible choices for coord = (50+1)*(50+1) - origin => 2601 coords
# pick2, -> 2601 pick 2 = 3,381,300 combos

def generate_coords(bound):
    out = []
    for x in range(bound+1):
        for y in range(bound+1):
            c = (x,y)
            out.append(c)
    return out[1:] # first entry is (0,0), so do not include

def valid_traingle(a,b):
    # 3 points of triangle, (0,0), A, B
    ## cannot use pyth tripls as some hyp. are not integers
    x1,y1 = a
    x2,y2 = b
    leg1 = (x1*x1 + y1*y1)
    leg2 = (x2*x2 + y2*y2)
    dx,dy = abs(x1-x2), abs(y1-y2)
    leg3 =(dx*dx + dy*dy)

    tri = sorted([leg1,leg2,leg3])
    return tri[0] + tri[1] == tri[2]

def solve(bound):
    s = time.time()

    coords = generate_coords(bound)
    right_triangles = 0
    for a,b in itertools.combinations(coords,2):
        if valid_traingle(a,b):
            right_triangles+=1
    e = time.time()
    print(f"{right_triangles} right triangles found within box {bound}x{bound}, {1000*(e-s):f} micro-seconds")

solve(2)
# 14 right triangles found within box 2x2, 0.022888 micro-seconds
solve(50)
# 14234 right triangles found within box 50x50, 1427.109003 micro-seconds
