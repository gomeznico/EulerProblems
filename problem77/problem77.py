"""
Problem 77

It is possible to write ten as the sum of primes in exactly five different ways:

&7 + 3
&5 + 5
&5 + 3 + 2
&3 + 3 + 2 + 2
&2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

import math
import time

primes = [2,3]
def is_prime(n,primes):
    for p in primes:
        if n%p ==0: return False
        if p>math.sqrt(n): break
    return True

def add_primes_upto(limit,primes):
    n = primes[-1]+2
    while primes[-1] < limit:
        if is_prime(n,primes): primes.append(n)
        n+=2




def possible_sums(n,primes,memo={}):
    if n == 1: return set()
    if n == 2: return set([(2,)])
    if n == 3: return set([(3,)])

    if n in memo: return memo[n]


    combos = set()
    ## make sure primes goes up to n
    add_primes_upto(n,primes)
    if is_prime(n,primes): combos.add((n,))

    for p in primes:
        if p>n: break
        ## get all combos starting with prime p

        prev_combos = possible_sums(n-p,primes,memo)

        new = [tuple(sorted(list(c) +[p])) for c in prev_combos]
        combos.update(new)
        # add (i, n-i)
        # combos.add(tuple(sorted([i,diff])))

    memo[n] = combos
    return combos


limit = 5_000
s = time.time()
l = 1
i=1
while l<limit:
    i+=1
    l = len(possible_sums(i,primes))
e = time.time()

print(f'first integer >{limit:_} ways to be written as sum of primes: {i}!, answer found in {e-s:.2f} seconds.')
print(f'{i} has {l:_} ways of being written as a sum of primes')

# first integer >5_000 ways to be written as sum of primes: 71!, answer found in 0.12 seconds.
# first integer >50_000 ways to be written as sum of primes: 104!, answer found in 2.45 seconds.
# first integer >100_000 ways to be written as sum of primes: 114!, answer found in 5.38 seconds.
# first integer >500_000 ways to be written as sum of primes: 142!, answer found in 51.47 seconds.
