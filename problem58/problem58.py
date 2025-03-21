"""
Problem 58

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 approx 62%.
If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""
import math
# get all diag. numbers based on num of squares

def diag_numbers(n,prev=None):
    # n number of squares
    if n == 1: return [1]

    side_len = 2*n -1
    if prev == None:
        prev = diag_numbers(n-1)
    last = max(prev)
    new = [last+(side_len-1),last+2*(side_len-1),last+3*(side_len-1),last+4*(side_len-1)]
    out = prev[::] + new
    return out

def is_prime(n,primes):

    for factor in primes:
        if factor > math.sqrt(n):break
        if n%factor == 0: return False
    return True

def problem58(fraction):
    n = 2
    side_length = 2*n -1

    primes = [2,3,5,7]
    diag = diag_numbers(n)
    num_prime = 3


    while num_prime/len(diag) >= fraction:
        # add one more sq
        n+=1
        side_length = 2*n -1
        diag = diag_numbers(n,diag)
        if n%100 == 0: print(n)


        # add primes up to sqrt of last diag
        num = primes[-1]+2
        while primes[-1] < math.sqrt(diag[-1]):
            if is_prime(num,primes): primes.append(num)
            num+=2

        #check newest diag. nums
        for num in diag[-4:]:
            if is_prime(num,primes): num_prime+=1


    # when less than frac
    # print(diag)

    print(num_prime/len(diag), len(diag))
    print(side_length)

fraction =0.10
problem58(fraction)
