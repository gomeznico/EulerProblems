"""
Problem 78

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O


p(5)
5
4 1
3 2
3 1 1
2 2 1
2 1 1 1
1 1 1 1 1
Find the least value of n for which p(n) is divisible by one million.
"""
import time
import math

## v similiar to problem 76, where p(5):
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# only need to add the 'self' as an additional way

# f(n) = g(n,1) + g(n,2) + ...g(n, n-1)
# g(n,1) = 1        combo of {1,1,1,...} n instances of 1
# g(n,n-1) = 1      combo of {n-1, 1}
# g(n,2) = n//2     combo of {2,1,1,..}, {2,2,1,1...}, {2,2,2,1...} etc.
# g(n, x) where n-x == x+1 => return f(n-x)
# x<n/2 ,   g(n,x) = g(n-x,1) + g(n-x,2) + ... g(n-x,x)   ex: g(8,3) = g(5,1) + g(5,2) + g(5,3)
# x>= n/2 , g(n,x) = f(n-x) + 1                           ex: g(8,5) = f(3) +

## use wikipedia partition function
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)
# p(n) = summation k[all non-zero integers] -> (-1)^(k+1) * p(n - k*(3k-1)/2) ... => p(n-1) + p(n-2) - p(n-5) ....
#  k = 1,-1, 2,-2, 3,-3....


def partion(n,memo={}):
    if n < 0: return 0
    if n == 1 or n==0: return 1
    if n in memo: return memo[n]

    def term(k):
        return k*(3*k-1)//2
    sum = 0
    k = 1
    term1 = term(k)
    term2 = term(-k)

    # a = (-1)^(k+1)
    #  for k = 1, a1, a2 are both +
    a1 = 1  # (-1)^2
    a2 = 1  # (-1)^0

    ## keep summing until both are 0 or less
    while n-term1 >=0 or n-term2>=0:
        sum += a1*partion(n-term1,memo)
        sum += a2*partion(n-term2,memo)

        k+=1
        term1,term2 = term(k),term(-k)
        # a1,a2 = pow(-1,k+1),pow(-1,-k+1)
        # a1,a2 = + if k is odd
        # a1,a2 = - if k is even

        if k%2 == 0:
            a1,a2 = -1,-1
        else:
            a1,a2 = 1,1
    memo[n] = sum
    return sum

def solve(factor):
    ## iterate thorugh i until result is
    # p(n) = count_combos(n) +1
    s = time.time()
    memo = {}
    ans,n = 1,1
    while ans%factor != 0 and n<factor:
        n+=1
        ans = partion(n,memo)
        if n%10_000 == 0: print(n, ans)
    e = time.time()
    print(f'first int to have num of combos divisible by {factor:_}: {n}  answer found in {e-s:.2f} seconds')
    print(f'number of combos is {ans}')

factor = 1_000_000
solve(factor)
