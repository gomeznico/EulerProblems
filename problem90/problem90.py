"""
Problem90

Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.
For example, the square number 64 could be formed:


In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.
For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.
However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.
In determining a distinct arrangement we are interested in the digits on each cube, not the order.
{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.
How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?
"""
import itertools,time
## Brute Force,
# find all combos of 2 dice, check if it is possible to create all squares.
# 9 distinct digits req'd for all perf. squares. Cannot have 2 of same die
# possibilities for each die = 10*9*8*7*6*5 => 151,200 possible permutations, but we only care about combos: (012345)==(543210)
# from 10, pick 6 -> C(n,r) = n!/(r!*(n-r)!) = 210 only
# different combos of 2 die == (210*210)/2 = 22050 possible pairs of die to check
# from 210 pick 2 -> 21945 combos of 2 die to check
def can_make_squares(die1,die2):

    squares = ['01','04','09','16','25','36','49','64','81']

    for sq in squares:
        a,b =sq[0],sq[1]
        if (a in die1 and b in die2) or (b in die1 and a in die2): continue
        return False
    return True

def create_dies():
    digits = '0123456789'
    return set(itertools.combinations(digits,6))
    # 210 dice with distinct 6 and 9


def solve():
    count = 0
    valid = 0
    s = time.time()
    dice = create_dies()
    print(len(dice))
    for die1,die2 in itertools.combinations(dice,2):
            # (1,2,3,4,5,6) is functionally the same as (1,2,3,4,5,9) but are considered distinct die
            # account for by 'extending' set with the flipped 6/9 as relevant, and using that as input
            if '6' in die1: die1 += ('9',)
            elif '9' in die1: die1 += ('6',)

            if '6' in die2: die2 += ('9',)
            elif '9' in die2: die2 += ('6',)



            count+=1
            if can_make_squares(die1,die2):
                valid+=1
    e = time.time()
    print(f"Found {valid} valid dice pairs, out of {count} total pairs.  {e-s:f} seconds elapsed")

solve()
# found 1217 valid dice pairs, out of 21945 total pairs.  0.019211 seconds elapsed




