"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23
3
7 4
2 4 6
8 5 9 3

what about the folliwing triangle

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23


"""
from copy import deepcopy
triangle ="""75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

sums =[]
## 15 rows, 14 choices

triangle = triangle.split('\n')

for i,line in enumerate(triangle):
    # arr = [int(x) for x in line.split(' ')]
    triangle[i] = [int(x) for x in line.split(' ')]
    sums.append([0 for x in line.split(' ')])


print(sums)
# go left, maintain i, go right i+1
# choosing maximum at each choice is not necessarily the best
# do BFS and keep track of max dist/ pathing


def max_sum(traingle_array,row,ind):
    val = traingle_array[row][ind]
    print(val)
    if row+1 == len(traingle_array):
        return val
    else:
        left_max = max_sum(traingle_array,row+1,ind)
        right_max = max_sum(traingle_array,row+1,ind+1)
        return val+ max(left_max,right_max)

# print(max_sum(triangle,0,0))

def bottomup(triangle):
    # start at second to last row, add the max of the two children below
    # then move up the triangle
    for row_i in range(len(triangle)-2,-1,-1):
        row = triangle[row_i]
        for col_i in range(len(row)):
            triangle[row_i][col_i] += max(triangle[row_i+1][col_i], triangle[row_i+1][col_i+1])
    return triangle[0][0]

print(bottomup(triangle))








