"""
Problem 67

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is23.

3
7 4
2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.
NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2^99 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

triangle = open('problem67/0067_triangle.txt', 'r').read()[0:-1]
test = """3
7 4
2 4 6
8 5 9 3"""



def parse(input:str):
    input = input.split('\n')
    out = []
    for line in input:
        row = [int(n) for n in line.split()]
        out.append(row)
    return out

# use DP to get largest sum
# assume you have max possible sum for each ending route in n-1 row.
# then for nth row, add appropriately
def DP(triangle:list,row:int,memo:dict={}):
    # output is array of the max_values to each

    # base case:
    if row == 0:
        memo[row] = triangle[row]
        return memo[row]

    if row in memo:
        return memo[row]

    else:
        prev_sums = DP(triangle,row-1, memo) + [0]
        vals = triangle[row]
        out = ['']*len(vals)
        for i,val in enumerate(vals):
            prev1, prev2 = 0,prev_sums[i]
            if i>0: prev1 = prev_sums[i-1]
            out[i] = val+max(prev1,prev2)
        memo[row] = out
        return out

input = parse(triangle)
row = len(input)-1
# print(DP(input,row))
print(max(DP(input,row)))
# 7273 correct!















