"""
Problem 85

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

OOO
OOO

XOO
OOO

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
"""
import math, time

## start with single row
#  [][][][][] => 5 1x blocks + 4 2x blocks + 3 3x blocks....
# for single row of w, num of rectangles = triangle(w)


## for double row (n! wide, h rows)
# [][][][][]
# [][][][][]
#  2x w! for single rows
# + 1x w! for a 'row' that is 2blocks high
# now to accunt for 'vert' blocks...
# wait, block that is 2 high by 1 wide is already counted in the 1x doublerow...

## up to 4xrow
# [][][][][]
# [][][][][]
# [][][][][]
# [][][][][]

# single row = h*tri(w)
# double row = 3*tri(w)
# triple row = 2*tri(w)
# double row = 1*tri(h)
# num rect = (1+2+3+4)*tri(w)  => tri(w)*tri(h)

def tri(n):
    # out = n + n-1 + n-2...+1
    return n*(n+1)//2


def num_rectangles(w,h):
    return h*w*(h+1)*(w+1)//4
    # return  tri(w)*tri(h)


## for target of 2mil,
## a single row of n~sqrt(4mill) => ~ 2000
# num_rectangles(1,2000) => 2001000
# num_rectangles(95,95) => 20793600

def solve(target):
    #  target ~= n*(n+1)//2
    #  2*target ~= n*(n+1)
    s = time.time()
    ceil = int(math.sqrt(2*target))+1
    best = (0,0)
    for h in range(1,100):
        for w in range(h,ceil):
            # func(h,w) = func(w,h), so only need to check one way


            num = num_rectangles(h,w)
            if abs(num - target) < abs(best[0]-target):
                best = (num,h,w)

            if num>target:
                break
                # increasing width further will only bring farther from from target now
                # go to next hieght and start inner loop of w again
                
    num,h,w = best
    e = time.time()
    print(f"best area is {h*w} in {w}x{h} rectangle.  found in {e-s:f} seconds")

solve(2_000_000)
# brute force, check all combos:
# best area is 2772 in 36x77 rectangle.  found in 0.435016 seconds
# break out of inner for loop once num > target: ~200x faster!
# best area is 2772 in 36x77 rectangle.  found in 0.002356 seconds
