"""
Problem 100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(text{BB}) = (15/21) * (14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 10^{12} = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""
import time
from math import sqrt, gcd

# b = num blue
# r = num red

# b/(b+r) * (b-1)/(b+r-1) = 1/2
# 2b*(b-1) = (b+r)(b+r-1)
# 2*b*(b-1) - (T)(T-1) = 0
# looks similiar to Pell equation...

# 2(b^2 - b) - (t^2 - t) = 0
# complete the sq
# 2 * ([b-1/2]^2 - 1/4) - ([t-1/2]^2 - 1/4) = 0
# mult by 4:
# 8([b-1/2]^2 - 1/4) - 4([t-1/2]^2 - 1/4) = 0
# 8[  ]^2 - 2 - 4[   ]^2 + 1 = 0
# 8[  ]^2 - 4[  ]^2 = +2-1 = 1

# y = 2n-1
# x = 2t-1

# 8*(y/2)^2 - 4*(x/2)^2 = 1
# 2y^2 -x^2 = 1
# x^2 - 2y^2 = -1 <=== Pell Eq

# use sqrt(2) cont. fraction to solve
# https://mathworld.wolfram.com/PellEquation.html
# x,y = p_r, q_r for r = odd
# p_n / q_n = nth convergent
# [a_0, a_1, ... a_r, 2*a_0]
# for sqrt(2) -> [a_0, ...] = [1,2].  2 repeats immediately
# for sqrt(2) -> r = 0 alctually
# hence p, q solution = 1,1
# generate family of solution based of 1,1...

# x = 2t-1      = [ (p+q*sqrt(D))^n + (p-q*sqrt(D))^n ]/ 2
# y = 2blue-1   = [ (p+q*sqrt(D))^n - (p-q*sqrt(D))^n ]/ 2*sqrt(2)
# where n is odd

# total = (x+1) //2
# number blue = (y+1)//2

# at n = 3, total, blue = 4 ,3 -Valid!
# at n = 5, total, blue = 21 ,15 -Valid!
# at n = 7, total, blue = 120, 85 Valid!

def solve_x(n):
    # x = 2t-1      = [ (p+q*sqrt(D))^n + (p-q*sqrt(D))^n ]/ 2
    # y = 2blue-1   = [ (p+q*sqrt(D))^n - (p-q*sqrt(D))^n ]/ 2*sqrt(2)


    # a = 1, and b = sqrt(2)
    # using bin expansion, and knowing n is always odd
    # (a+b)^n -> a^n + [coeff]a^n-1 * b + ... + b^n
    #   +
    # (a-b)^n -> a^n - [coeff]a^n-1 * b + ... - b^n

    # every other term cancels out
    # numerator = 2* [a^n + (coeff)*a^n-2 * b^2 + (coeff)*a^n-4 * b^4 ... ]
    # only count 'even' terms, 0th, 2nd, 4th...


    # coeef. based on pascals triangle
    #      1
    #     1,1        (a+b)
    #    1,2,1       (a+b)^2
    #   1,3,3,1      (a+b)^3
    #  1,4,6,4,1     (a+b)^4
    #1,5,10,10,5,1   (a+b)^5

    #
    #get coeff
    arr,level = [1,1], 1
    while level != n:
        arr = [0] + arr + [0]
        new_arr = [a+b for a,b in zip(arr, arr[1:])]
        arr = new_arr
        level+=1

    coeff = arr
    num = 0
    for i in range(len(coeff)):
        #term = a^n-i * b^i * coeff
        # term = 1 * sqrt(2)^i
        if i%2 == 0:
            term = coeff[i]*1*pow(2,i//2)
            num+= term
    num *= 2
    den = 2
    return num//den

def solve_y(n):
    # x = 2t-1      = [ (p+q*sqrt(D))^n + (p-q*sqrt(D))^n ]/ 2
    # y = 2blue-1   = [ (p+q*sqrt(D))^n - (p-q*sqrt(D))^n ]/ 2*sqrt(2)


    # a = 1, and b = sqrt(2)
    # using bin expansion, and knowing n is always odd
    # (a+b)^n -> a^n + [coeff]a^n-1 * b + ... + b^n
    #   - (subtract)
    # (a-b)^n -> a^n - [coeff]a^n-1 * b + ... - b^n

    # every other term cancels out
    # only count 'odd' terms, 1th, 3nd, 4th...

    # numerator = 2* [(coeff)*a^n-1 * b^i + (coeff)*a^n-3 * b^3 ... b^n ]
    # denom = 2*b = 2*sqrt(2)
    # 2 in the front gets divided out
    # each term in num gets one exp. removed from division of b in denom

    # a = 1
    # ans = [(coeff) * b^(1-1) + (coeff)* b^(3-1) ... b^(n-1) ]

   # coeef. based on pascals triangle
    #      1
    #     1,1        (a+b)
    #    1,2,1       (a+b)^2
    #   1,3,3,1      (a+b)^3
    #  1,4,6,4,1     (a+b)^4
    #1,5,10,10,5,1   (a+b)^5

    #get coeff
    arr,level = [1,1], 1
    while level != n:
        arr = [0] + arr + [0]
        new_arr = [a+b for a,b in zip(arr, arr[1:])]
        arr = new_arr
        level+=1

    coeff = arr
    # print(coeff)
    num = 0
    for i in range(len(coeff)):
        #term = a^n-i * b^i * coeff
        # term = 1 * sqrt(2)^i
        if i%2 == 1:
            # print(coeff[i], i)
            term = coeff[i]*1*pow(2,(i-1)//2)
            num+= term

    return num

def solve():
    s = time.time()
    limit = pow(10,12)
    ## go through diff. n's until
    n = 1
    total = (1+solve_x(n))//2
    while total < limit:
        n+=1
        total = (1+solve_x(n))//2
        # blue = (1+solve_y(n))//2


    # total now greater than limit
    # get blue count
    print(f'{n} steps taken to get to arrangement with {total:_} total chips')
    blue = (1+solve_y(n))//2
    e = time.time()
    print(f"number of blue chips for first arrangement above 10^12 is {blue}. {1000*(e-s):f} micro-seconds elapsed")

solve()
# number of blue chips for first arrangement above 10^12 total chips is 756_872_327_473. 0.739098 micro-seconds elapsed
