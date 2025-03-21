"""
Problem 53

There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation, displaystyle binom:   (5 , 3) = 10.
In general, (n, r) = n! /r!(n-r)!, where
r <= n,
n! = n * (n-1) * ... * 3 * 2 * 1,
and 0! = 1.

It is not until n = 23, that a value exceeds one-million:(23 , 10) = 1144066.
How many, not necessarily distinct, values of   (n, r) for 1 <=n <= 100, are greater than one-million?
"""
from math import factorial

# total possibilities of r and n
# n [1,100] -> 100 poss.
# r [1,n] -> ~ 100 poss
# total calcs = 100*100 = 10,000


## brute force
def choose_c_from_n(c,n):
    val = factorial(n) // (factorial(c)* factorial(n-c))
    return val

minimum = 1_000_000
count = 0
for n in range(23,900):
    for c in range(1,n+1):
        # print(choose_c_from_n(c,n))
        if choose_c_from_n(c,n) > minimum:
            count+=1
print(count)

## being clever, lets say boundary is much much larger, and want to calculate from c and n only
# for each c, use binary search to find where 1st r resulting in 1mil is.
# use that to count how many r's reult in over 1mil, add to count
# repeat for each c

def bin_search(n,num_selections):
    # find lowest c where c,n is over val
    low,high = 0,n
    pivot = low + (high-low)//2
    while low<=high:
        val = choose_c_from_n(pivot,n)
        if val == num_selections:
            return pivot
        if val < num_selections:
            low = pivot+1
        else:
            high = pivot-1
        pivot = low + (high-low)//2
    if low>n:
        return -1
    return low

count = 0
for n in range(1,900):
    c = bin_search(n,minimum)
    if c > -1:
        count += ((n+1)/2 - c)*2
print(count)

# print(choose_c_from_n(8,25))


