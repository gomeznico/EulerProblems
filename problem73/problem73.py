"""
Problem 73

Consider the fraction, dfrac n d, where n and d are positive integers. If n lt d and operatorname{HCF}(n, d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d le 8 in ascending order of size, we get:

1/8 ,1/7, 1/6, 1/5, 1/4, 2/7 , 1/3 , 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.
How many fractions lie between dfrac 1 3 and dfrac 1 2 in the sorted set of reduced proper fractions for d < 12,000?
"""

import time
import math
from collections import defaultdict

## Brute Force:
# generate all fract, and order them.  Then count how many are between 1/3->1/2

## Reduced Brute Force
# O(n2)*O(logn)
# generate all frac between 1/3 and 1/2
# loop d 1->limit:
    # loop n [n_1,n_2] where n_1/d > 1/3 and n_2/d < 1/2
    # if reduced frac, add to count
# number of reduced fracs with d<=12_000  between 1/3 and 1/2, calc`d in 11.02 sec : 7295372

## Seive Erastonos approach
# create dict that holds all n's that make reduced fract

def sieve_of_eratosthenes(limit):
    # O(logn) time
    if limit < 2:
        return []

    primes = [True] * (limit + 1)  # Create a boolean array
    primes[0], primes[1] = False, False  # 0 and 1 are not prime

    for num in range(2, int(limit ** 0.5) + 1):
        if primes[num]:  # If num is prime, mark its multiples as non-prime
            for multiple in range(num * num, limit + 1, num):
                primes[multiple] = False

    return [num for num, is_prime in enumerate(primes) if is_prime]

def sieve_smallest_prime_factor(limit,primes):
    # O(logn) time
    ## generate arr of smallest prime factor at each index
    spf = [1]*(limit+1)
    for p in primes:
        # fill spf[i] with p for every multiple of p
        spf[p] = p
        for multiple in range(p*p, limit+1, p):
            spf[multiple] = p
    return spf

def prime_factors(n,spf):
    # O(logn) time
    out = set()
    num = n
    while spf[num] != 1:
        f = spf[num]
        out.add(f)
        num//=f
    return out

def pre_calc_pfactors(limit,spf):
    # O(n*logn) time
    factors = defaultdict(set)
    for n in range(1,limit+1):
        factors[n] = prime_factors(n,spf)
    return factors

def is_reduced_frac(num,den,factors):
    # if reduced fraction, prime factors of num and den will be different
    pf1 = factors[num]  # O(1)
    pf2 = factors[den]  # O(1)
    return pf1.intersection(pf2) == set()   # O(log)

def solve_BF(limit):
    # O(n2)*O(logn)
    primes = sieve_of_eratosthenes(limit)
    spf = sieve_smallest_prime_factor(limit,primes)
    factors = pre_calc_pfactors(limit, spf)
    print('prepopulated primes, spf, factorizations...')

    s = time.time()
    out = 0
    low = 1/3
    high = 1/2

    for d in range(4,limit+1):
        n_start = int(low*d) +1
        n_end = int(high*d)

        for n in range(n_start,n_end+1):
            if is_reduced_frac(n,d,factors):
                # print(n,d)
                out+=1
    e = time.time()
    print(f'number of reduced fracs with d<={limit:_}  between 1/3 and 1/2, calc`d in {e-s:.2f} sec : {out}')

def solve_Seive(limit):

    s = time.time()
    out = 0
    low = 1/3
    high = 1/2

    #prepopulate dict
    # O(n2)
    valid_n = {}
    for d in range(2,limit+1):
        valid_n[d] = set(range(1,d))    # {1,2,3...d-1}
        # will filter d as looped through again
    print('prepopulated dict...')

    out = 0
    for d in range(2,limit+1):
        # ex: d=8,
        # n_low = 1/3*8 = 2.66, , all filtered n's msut be >2.66
        # n_high = 1/2*8 = 4, , all filtered n's msut be <4
        n_low = low*d
        n_high = high*d

        # filter all n's in valid_n[d] base on above range
        out += len([n for n in valid_n[d] if n_low<n<n_high])

        # print(d,valid_n[d])

        ## filter multiples of n/d from larger d's
        for i in range(2, (limit//d) + 1):
            a = [n*i for n in valid_n[d]]
            valid_n[d*i].difference_update(a)

    e = time.time()
    print(f'number of reduced fracs with d<={limit:_}  between 1/3 and 1/2, calc`d in {e-s:.2f} sec : {out}')

def solve_Seive_V2(limit):

    s = time.time()
    out = 0
    low = 1/3
    high = 1/2

    #prepopulate dict, but filter to keep only n's between low/high
    valid_n = {}
    for d in range(2,limit+1):
        n_low = int(low*d)+1
        n_high = int(high*d)+1
        valid_n[d] = set(range(n_low,n_high))
    print('prepopulated dict...')

    out = 0
    for d in range(2,limit+1):
        ## need to start with 2 to correctly
        if d>2:
            out += len(valid_n[d])

        # print(d,valid_n[d])

        ## filter multiples of n/d from larger d's
        for i in range(2, (limit//d) + 1):
            a = [n*i for n in valid_n[d]]
            valid_n[d*i].difference_update(a)
    e = time.time()
    print(f'number of reduced fracs with d<={limit:_}  between 1/3 and 1/2, calc`d in {e-s:.2f} sec : {out}')


# solve_BF(12_000)
# limit = 1000 , 0.02 sec
# limit = 10_000 , 2.02 sec
# limit = 25_000 , 13.02 sec
# limit = 50_000
# number of reduced fracs with d<=12_000  between 1/3 and 1/2, calc`d in 2.86 sec : 7295372

# solve_Seive(12_000)
# limit = 1000 , 0.04 sec
# limit = 10_000 , 11.35 sec
# limit = 25_000 , 229.19 sec
# limit = 50_000 
# number of reduced fracs with d<=12_000  between 1/3 and 1/2, calc`d in 19.80 sec : 7295372


solve_Seive_V2(12_000)
# limit = 1000 , 0.01 sec
# limit = 10_000 , 0.73 sec
# limit = 25_000 , 7.72 sec
# limit = 50_000 , 87.82 sec
# number of reduced fracs with d<=12_000  between 1/3 and 1/2, calc`d in 0.94 sec : 7295372



