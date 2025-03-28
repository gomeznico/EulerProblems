"""
Problem 87

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""
import math, time

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

def prime_squares(primes,limit):
    out = []
    for p in primes:
        num = p*p
        if num > limit: break
        out.append(num)
    return out

def prime_cubes(primes,limit):
    out = []
    for p in primes:
        num = p*p*p
        if num > limit: break
        out.append(num)
    return out

def prime_fourths(primes,limit):
    out = []
    for p in primes:
        num = p*p*p*p
        if num > limit: break
        out.append(num)
    return out

##brute force all combos of each until limit reached
# no common numbers between squares, cubes and fourths of primes, so all combos are unique

def solve(limit):

    s = time.time()
    primes = sieve_of_eratosthenes(int(math.sqrt(limit))+1)
    print(f'generated {len(primes)} primes')

    squares = prime_squares(primes,limit)
    cubes = prime_cubes(primes,limit)
    fourths = prime_fourths(primes,limit)

    nums = set()
    for a in squares:
        for b in cubes:
            for c in fourths:
                num =a+b+c
                if num < limit:
                    # 1139575 combos of abc are < 50mil
                    # some numbers are repeated so use set
                    nums.add(num)
    e = time.time()
    print(f'{len(nums):_} numbers below {limit:_} can be written as sum of a prime sq, cube, and fourth power: {e-s:f} seconds')

solve(50_000_000)
# 1_097_343 numbers below 50_000_000 can be written as sum of a prime sq, cube, and fourth power: 0.194908 seconds
