"""
Problem 88

A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a_1, a_2, ..., a_k} is called a product-sum number: N = a_1 + a_2 + ... + a_k = a_1 * a_2 * ... * a_k.
For example, 6 = 1 + 2 + 3 = 1 * 2 * 3.
For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 * 2 = 2 + 2
k=3: 6 = 1 * 2 * 3 = 1 + 2 + 3
k=4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6
Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.
In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?
"""
import math, time
from collections import defaultdict

def prod(arr):
    n = 1
    for i in arr:
        n*=i
    return n

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
    out = []
    num = n
    while spf[num] != 1:
        f = spf[num]
        out.append(f)
        num//=f
    return out

def combos_of_factors(tup):
    # arr is at least len = 2
    out = set([tup])
    if len(tup) == 1:
        return out
    # if len(tup) == 2:
    #     a = (tup[0]*tup[1],)
    #     out.add(a)
    #     return out
    # [a,b,c] => create subarrays
    created = set()
    for i,el in enumerate(tup):
        pre_arr = list(tup[0:i])
        pos_arr = list(tup[i+1:])
        for j in range(len(pos_arr)):
            a = pos_arr[::]
            a[j] *= el
            a = pre_arr+ a[::]
            a = sorted(a)
            created.add(tuple(a))

    out.update(created)
    if len(tup)==2:
        return out

    ## if created tuples are len=2 or greater, then get sub arrays for each created tuple
    for t in created:
        out.update(combos_of_factors(t))
    return out

def prod_sum_arrays(n,spf):
    # produce arrays that satisfy prod(arr)==sum(arr)

    factors = prime_factors(n,spf)
    all_factorizations = combos_of_factors(tuple(factors))

    possible_ks = []
    for arr in all_factorizations:
        if len(arr)==1: continue
        # n = sum(arr) + [1]*x
        test_arr = [1]*(n-sum(arr)) +list(arr)
        # print(test_arr)
        k = len(test_arr)
        possible_ks.append(k)

    return sorted(possible_ks)

def solve(max_k):
    ## find all k's up to
    s = time.time()
    all_ks = list(range(2,max_k+1))
    curr_limit = 100
    primes = sieve_of_eratosthenes(curr_limit)
    spf = sieve_smallest_prime_factor(curr_limit,primes)
    min_prod_sum = defaultdict(int)

    n = 4
    while True:
        possible_ks = prod_sum_arrays(n,spf)
        for k in possible_ks:
            # first k found is be definition the smallest
            if k not in min_prod_sum:
                min_prod_sum[k] = n


        # check if all entries up to max_k are found
        keys = [a for a in min_prod_sum.keys() if a<=max_k]
        if all_ks == sorted(keys):
            checksum = sum(set(min_prod_sum[a] for a in min_prod_sum if a<=max_k))
            break

        n+=1
        ## add to primes/prime factorization table if reached limit
        if n>=curr_limit:
            curr_limit = 2*n
            primes = sieve_of_eratosthenes(curr_limit)
            spf = sieve_smallest_prime_factor(curr_limit,primes)
            print(f'increased spf table to {curr_limit}')
        if n%1_000==0:
            print(f"checked n up to {n}, max_found k is k={max(keys)}")


    e = time.time()
    print(f"{checksum} is sum of all min_prod_sums for k<= {max_k} found in {e-s:f} seconds")


# solve(6)
# solve(12)
# solve(100)
# solve(1_000)
# solve(10_000)
# solve(12_000)
# solve(20_000)

# 30 is sum of all min_prod_sums for k<= 6 found in 0.000070 seconds
# 61 is sum of all min_prod_sums for k<= 12 found in 0.000088 seconds
# 2061 is sum of all min_prod_sums for  k<=   100 found in 0.002207 seconds
# 93063 is sum of all min_prod_sums for k<=   1000 found in 0.318752 seconds
# 5441890 is sum of all min_prod_sums for k<= 10000 found in 66.484353 seconds
# 7587457 is sum of all min_prod_sums for k<= 12000 found in 113.578494 seconds
# 18858239 is sum of all min_prod_sums for k<= 20000 found in 455.751629 seconds


## method2 to get other prod/sum arrays
# much much faster since factorizations based on divisors of n, rather than all combos of multiplying prime factors

def possible_factorizations(orig_n, n, Prod:int=1, Sum:int=0, count:int=0, memo = {}):
    """
    orig_n  : original n at intitilizations of function
    n       : current n being considered,
    prod    : product of divisors used to get to current n
    sum     : sum of divisors used to get to current n
    count   : number of divisors used to get to curr n
    """
    key = (orig_n,n,Prod,Sum, count)
    if key in memo:
        return memo[key]

    elif Prod>orig_n or Sum>orig_n:
        return
    if Prod == Sum == orig_n:
        # valid array found of length count
        memo[key] = [count]

    if n == 1:
        # have used all divisors, and prod by definition must == orig_n
        # 'fill' array with 1's to get Sum == Prod
        k = count + (Prod - Sum)
        memo[key] = [k]
        return memo[key]

    out = []
    for div in range(2,n+1):
        if n%div==0:
            out += possible_factorizations(orig_n,n//div, Prod*div, Sum+div, count+1,memo)
    memo[key] = out

    if (Prod,Sum,count) == (1,0,0):
        # turn final output into set to avoid duplicates
        out = set(memo[key])
        out.discard(1)
        return out

    return memo[key]

def solveV2(max_k):
    ## find all k's up to max_k
    s = time.time()
    all_ks = list(range(2,max_k+1))
    min_prod_sum = defaultdict(int)

    n = 4
    while True:
        possible_ks = possible_factorizations(n,n)
        for k in possible_ks:
            # first k found is be definition the smallest
            if k not in min_prod_sum:
                min_prod_sum[k] = n

        # check if all entries up to max_k are found
        keys = [a for a in min_prod_sum.keys() if 2<=a<=max_k]
        if all_ks == sorted(keys):
            checksum = sum(set(min_prod_sum[a] for a in min_prod_sum if a<=max_k))
            break

        n+=1
        if n%1_000==0:
            print(f"checked n up to {n}, max_found k is k={max(keys)}")

    e = time.time()
    print(f"{checksum} is sum of all min_prod_sums for k<= {max_k} found in {e-s:f} seconds")

n=12
print(possible_factorizations(n,n))

solveV2(6)
solveV2(12)
solveV2(100)
solveV2(1_000)
solveV2(10_000)
solveV2(12_000)
solveV2(20_000)
# 30 is sum of all min_prod_sums for k<= 6 found in 0.000041 seconds
# 61 is sum of all min_prod_sums for k<= 12 found in 0.000458 seconds
# 2061 is sum of all min_prod_sums for k<= 100 found in 0.001903 seconds
# 93063 is sum of all min_prod_sums for k<= 1000 found in 0.119677 seconds
# 5441890 is sum of all min_prod_sums for k<= 10000 found in 8.268610 seconds
# 7587457 is sum of all min_prod_sums for k<= 12000 found in 9.774260 seconds
# 18858239 is sum of all min_prod_sums for k<= 20000 found in 31.402883 seconds
