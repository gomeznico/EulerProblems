"""
Problem 99

Comparing two numbers written in index form like 2^{11} and 3^7 is not difficult, as any calculator would confirm that 2^{11} = 2048 lt 3^7 = 2187.
However, confirming that 632382^{518061} gt 519432^{525806} would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
import time, math
input = open('problem99/base_exp.txt','r').read()[0:-1].split('\n')

a,a1 = [632382, 518061]
b,b1 = [519432, 525806]

def solve(input):
    arr = []
    s = time.time()
    for i,line in enumerate(input):
        a,b = line.split(',')
        val = int(b)*math.log(int(a))
        arr.append((val,i+1))
    arr = sorted(arr)
    ans = arr[-1][1]
    e = time.time()
    print(f"the largest number is on line {ans}. found in {1000*(e-s):f} microseconds")

solve(input)






ans1 = a1*math.log(a)
ans2 = b1*math.log(b)

# print(ans1,ans2)

# print(b1-a1)
# # print(pow(b,b1-a1))

# div = math.gcd(a1,b1)
# print(a1//div, b1//div)
