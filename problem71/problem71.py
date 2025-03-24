"""
Problem 71

Consider the fraction,  n/d, where n and d are positive integers. If n < d and HCF(n,d)=1, it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d < 8 in ascending order of size, we get:

1/8 ,1/7, 1/6, 1/5, 1/4, 2/7 , 1/3 , 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that dfrac 2 5 is the fraction immediately to the left of dfrac 3 7.

By listing the set of reduced proper fractions for d < 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of dfrac 3 7.
"""
import math
import time

## brute force: O(n2)*gcd operator
# loop trhough n = [1->1mil]
#   get GCD for all vals less than n-> calculate all fractions and get one closest to 3/7

## targeted brute force:
# save val of 3/7 as target
# 1/3 is first val that is to the left of 3/7
# best = 1/3

# loop through n 1->limit
    # with chosen n, loop through d going down
    # d -> [start,end]
        # start at closest val below 3/7,
        # end is first val when d/n < best
        # if d/n is red. frac and best<d/n<3/7:
        # best



## determine GCD is 1 by cehcking prime factors?
## if prime factors of 2 num are diff. then 1 is GCD

def sieve_of_eratosthenes(limit):
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
    ## generate arr of smallest prime factor at each index
    spf = [1]*(limit+1)
    for p in primes:
        # fill spf[i] with p for every multiple of p
        spf[p] = p
        for multiple in range(p*p, limit+1, p):
            spf[multiple] = p
    return spf

def prime_factors(n,spf):
    out = set()
    num = n
    while spf[num] != 1:
        f = spf[num]
        out.add(f)
        num//=f
    return out

def is_reduced_frac(num,den,spf):
    # if reduced fraction, prime factors of num and den will be different
    pf1 = prime_factors(num,spf)
    pf2 = prime_factors(den,spf)
    return pf1.intersection(pf2) == set()

def solve(limit):

    s = time.time()
    primes = sieve_of_eratosthenes(limit)
    spf =sieve_smallest_prime_factor(limit,primes)
    e = time.time()
    print(f'generated {limit:_} primes in {e-s:.2f} sec')

    s = time.time()
    target = 3/7
    best = 1/3
    frac = (1,3)
    for d in range(4,limit+1):
        start_n = int(target*d)

        for n in range(start_n,0,-1):
            if n/d == 3/7: continue
            if n/d < best: break
            if is_reduced_frac(n,d,spf):
                best , frac = n/d , (n,d)
                break

    e = time.time()
    print(f'run thorugh {limit:_} in {e-s:.2f} sec')
    print(f'closest frac to the left of 3/7:  {frac[0]}/{frac[1]} ')

solve(1_000_000)
# solved in 0.46 sec, n / d = 428570 / 999997
