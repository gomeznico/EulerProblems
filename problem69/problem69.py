"""
Problem 69

Euler's totient function, phi(n) [sometimes called the phi function], is defined as the number of positive integers not exceeding n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than or equal to nine and relatively prime to nine, phi(9)=6.

n       Relatively Prime        phi(n)      n/phi(n)
2       1                       1           2
3       1,2                     2           1.5
4       1,3                     2           2
5       1,2,3,4                 4           1.25
6       1,5                     2           3
7       1,2,3,4,5,6             6           1.1666...
8       1,3,5,7                 4           2
9       1,2,4,5,7,8             6           1.5
10      1,3,7,9                 4           2.5

It can be seen that n = 6 produces a maximum n/phi(n) for nleq 10.
Find the value of n <=1,000,000 for which n/phi(n) is a maximum.
"""
import math
import time

def is_prime(n,primes):
    for f in primes:
        if n%f ==0: return False
        if f>math.sqrt(n): break
    return True

def prime_factors(n,primes):
    out = set()
    num = n
    for f in primes:
        if f>num: break
        while num%f == 0:
            out.add(f)
            num//=f
    return out-set([n])

def phi(n,primes_set,primes):
    if n in primes_set: return n-1
    ## get prime factors, then all multiples of prime factors
    pfactors = prime_factors(n,primes)
    # p_facotrs = {p1,p2,...}
    # phi(n) = n * (1-1/p1) * (1- 1/p2) * ...
    #        = n * (p1-1)/p1 * (p2-1)/p2 * ...
    # num = n*(p1-1)*(p2-1)*...
    # den = p1*p2*p3...
    def cumProd(arr):
        out = 1
        for a in arr:
            out*=a
        return out
    num = cumProd([(p-1) for p in pfactors] + [n])
    den = cumProd(pfactors)

    return num//den

def solve(limit):
    # generate primes up to limit
    primes = [2]
    for i in range(3,limit):
        if is_prime(i,primes):
            primes.append(i)

    primes_set=set(primes)

    val = 0
    ans = 0
    start = time.time()
    for n in range(2,limit+1):
        phi_val = phi(n,primes_set,primes)
        if n/phi_val>val:
            ans,val = n, n/phi_val
    end = time.time()
    print(f'going through {limit:_} values took {end-start:.4f} seconds')
    print(f'n val of {ans} results in highest n/phi = {val}')

limit = 1_000_000
# solve(limit)
# 10_000 vals->     0.0363 sec
# 100_000 vals>     1.5551 sec
# 1_000_000vals>    92.55 sec
# ans n=510510 , n/phi(n) = 5.539...


## REfactoring code to use faster functions:

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

def sieve_smallest_prime_factor(primes, limit):
    ## generate arr of smallest prime factor at each index
    spf = [1]*(limit+1)
    for p in primes:
        # fill spf[i] with p for every multiple of p
        spf[p] = p
        for multiple in range(p*p, limit, p):
            spf[multiple] = p
    return spf

def prime_factors(n,spf):
    out = set()
    num = n
    while spf[num] != 1:
        f = spf[num]
        out.add(f)
        num//=f
    return out -set([n])

def phi_v2(n,primes_set,spf):
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
    # phi(n) = n * (p1-1)/p1 * (p2-1)/p2 ..
    num = cumProd([n] + [(p-1) for p in pfactors])
    den = cumProd([p for p in pfactors])
    return num//den

def solve_refactored(limit):

    primes = sieve_of_eratosthenes(limit)
    primes_set = set(primes)
    spf = sieve_smallest_prime_factor(primes,limit)

    val = 0
    ans = 0
    start = time.time()
    for n in range(2,limit+1):
        phi_val = phi_v2(n,primes_set,spf)
        if n/phi_val > val:
            ans,val = n, n/phi_val
    end = time.time()
    print(f'going through {limit:_} values took {end-start:.4f} seconds')
    print(f'n val of {ans} results in highest n/phi = {val}')

limit = 1_000_000
solve_refactored(limit)
# 1_000_000 vals - > 1.45 sec
# ans n=510510 , n/phi(n) = 5.539...
