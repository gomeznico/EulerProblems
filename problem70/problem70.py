"""
Problem 70

Euler's totient function, phi(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, phi(9)=6.The number 1 is considered to be relatively prime to every positive number,
so phi(1)=1.
phi(2) = 2
phi(3) = 2
Interestingly, phi(87_109)=79_180, and it can be seen that 87109 is a permutation of 79180.
Find the value of n, 1 < n < 10^7, for which phi(n) is a permutation of n and the ratio n/phi(n) produces a minimum.
"""

import math
import time

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

def sieve_smallest_prime_factor(limit):
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

def phi(n):
    def cumProd(arr):
        out = 1
        for a in arr:
            out*=a
        return out

    if n==1: return 1
    if n in primes_set: return n-1
    ## get prime factors set
    pfactors = prime_factors(n,spf)

    # phi(m*n) = phi(m) * phi(n)

    # phi(n) = n* (1-1/p1) * (1-1/p2) ...
    # phi(n) = n * (p1-1)/p1 * (p2-1)/p2 ...

    num = cumProd([n] + [(p-1) for p in pfactors])
    den = cumProd([p for p in pfactors])
    return num//den

def is_permutation(a,b):
    return sorted(str(a)) == sorted(str(b))


# generate primes up to limit
limit = 10_000_000
s = time.time()
primes = sieve_of_eratosthenes(limit)
primes_set = set(primes)
spf = sieve_smallest_prime_factor(limit)
e = time.time()
print(f'generated primes/spf up to {limit:_} in {e-s:.2f} sec')

min_n = float('inf')
min_val = float('inf')

start = time.time()
for n in range(2,limit):
    if n%500_000 == 0: print(f'{n:_}')
    if n in primes_set: continue
    val = phi(n)
    if is_permutation(val,n) and n/val<min_val:
        min_n,min_val = n, n/val
end = time.time()
print(f'going through {limit:_} values took {end-start:.3f} seconds')
print(f'n val of {min_n:_} results in min n/phi = {min_val}')

## Brute Force:
# 1mill vals checked: min n = 783_169, time = 1.822 sec
# 5mill vals checked: min n = 4_696_009, time = 9.435 sec
# 10mill vals checked: min n = 8_319_823, time = 19.679 sec
