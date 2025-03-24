"""
Problem 72

Consider the fraction, dfrac n d, where n and d are positive integers. If n lt d and operatorname{HCF}(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d le 8 in ascending order of size, we get:
1/8 ,1/7, 1/6, 1/5, 1/4, 2/7 , 1/3 , 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.
How many elements would be contained in the set of reduced proper fractions for d le 1,000,000?
"""
import time
import math
from collections import defaultdict

## Brute Force: O(n2)*O(pfactors)
# loop d 1->limit:
#   loop n 1->d:
        # count how many combos of n,d are reduced

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
    pf1 = factors[num]
    pf2 = factors[den]
    return pf1.intersection(pf2) == set()



def solve(limit):

    ### Brute Force -
    # O(n2) * O(logn)
    # two nested for loops * prime factorization

    # s = time.time()
    # primes = sieve_of_eratosthenes(limit)
    # spf =sieve_smallest_prime_factor(limit,primes)
    # factors = pre_calc_pfactors(limit, spf)
    # e = time.time()
    # print(f'generated {limit:_} primes in {e-s:.2f} sec')

    # s = time.time()
    # for d in range(2,limit+1):
    #     d_count = 0
    #     for n in range(1,d):
    #         if is_reduced_frac(n,d,spf):
    #             # print(n,d)
    #             d_count+=1
    #     out += d_count
    # e = time.time()

   ##pre populate assuming all n's are valid
    valid_n = {}
    for d in range(2,limit+1):
        valid_n[d] = d-1
        # value is the count of irreducible n's
    print('prepopulated dict...')

    ## using Sieve of Eratosthenes approach
    # O(n)*O(logn)
    out = 0
    s = time.time()
    for d in range(2,limit+1):
        # if d%100_000==0: print(d)
        # once at d, valid[d] returns count of all irreducible n for given denom d
        out+= valid_n[d]
        for i in range(2,(limit)//d+1):
            # for each multiple of d, subtract valid[d] from its count
            # valid[2] = 1, remove 1 from each multiple of d=2
            # valid[3] = 2 (1/3 and 2/3), remove 2 from each multiple of d=3
            # valid[4] = 2 (1/4 and 3/4), 1 was subtracted already b/c of d=2,
            # so now subtract 2 from all multiplied of d=4...
            # ...
            # valid[8], was 7 but = 4, 7- v[2] - v[4] = 7 -1-2 = 4! and so on...
            valid_n[d*i] += -valid_n[d]
    e = time.time()
    print(f'number of reduced fracs with d<={limit:_} in {e-s:.2f} sec : {out}')

solve(1_000_000_00)
# number of reduced fracs with d<=1_000_000 primes in 4.36 sec : 303963552391




