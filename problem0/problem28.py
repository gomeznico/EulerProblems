"""
Starting with the number 1 and moving to the right in a clockwise direction a
5 by 5 spiral is formed as follows:


21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

it can be verified that the sum of the numbers on the diagonals is 101

what is the sum on the diagonals in a 1001 by 1001 spiral formed i the same way?
"""
import math
size = 1001
spiral = []
line = ['.']*size
for i in range(size):
    spiral.append(['.']*size)

spiral[size//2][size//2] = 1
# for line in spiral: print (line)
row,col = size//2, size//2
center = (row,col)


# perim -> 1,9,25,49 .. total squares
#         1^2 3^2 5^2 7^2...
# perim path is 4 sides each of a sim length
# side length is sqrt of starting number
    # i.e. for num 1, nex square is 3x3,
    #   for starting num 9-> next square is 5x5 -> sqrt(9) + 2
    #   for starting num 25, next square is 7x7 -> sqrt(5) + 2
#

def fill_perim(spiral,start_coord):
    row,col = start_coord
    start_num = spiral[row][col]
    side_length = int(math.sqrt(start_num)+2)
    # last_num = side_length*side_length
    directions = [(1,0), (0,-1), (-1,0),(0,1)]
    row,col = row,col+1


    side = 0
    num = start_num+1
    for k in range(4):
        ## hack for getting 1st side
        n=1
        if side==0: n=2

        for i in range(side_length-n):
            spiral[row][col] = num
            dr,dc = directions[side]
            row,col = row+dr,col+dc
            num+=1
        side+=1
    # get very last num
    spiral[row][col] = num
    # output coords for next spiral
    return(row,col)

coord = center
while coord != (0,size-1):
    coord = fill_perim(spiral,coord)
    print(spiral[coord[0]][coord[1]])
# for line in spiral: print (line)


def sum_of_diagonals(spiral):
    diag = set()
    for i in range(size):
        num1 = spiral[i][i]
        num2 = spiral[i][-1-i]
        diag.add(num1)
        diag.add(num2)
    print(sum(diag))
sum_of_diagonals(spiral)


"""
SOLUTION WITHOUT BUILDING SPIRAL
much faster and cleaner
"""

## very last num = 1001*1001
## 1 + 4nums+4nums+4nums....
## each set of 4 nums is the 4 corners of is sq
## last num of each sq = odd num^2
## 9 =3x3, 25 =5x5, 49=7x7
## for 9 sq, 4 numbers are 9,7,5,3 or also 9, 9-2, 9-2*2, 9-2*3
    # 2 is sidelenght -1

size = 1001
center = 1
def next_four_nums(prev_num):
    side_length = int(math.sqrt(prev_num) +2)
    n=side_length-1
    last_num = side_length*side_length
    ans=[last_num-n*3, last_num-n*2, last_num-n, last_num]  #orderd so greaetest num is last
    return ans

diag =[1]
while diag[-1] !=size*size:
    diag = diag+next_four_nums(diag[-1])
print(sum(diag))




