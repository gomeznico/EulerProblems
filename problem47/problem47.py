"""
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5.

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 * 7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
def is_prime(num,primes):
    if num ==2: return True
    for factor in primes:
        if num%factor == 0: return False
    return True


def prime_factors(num,primes):
    #  primes is arr of primes less than num
    factors = set()
    while num != 1:
        for p in primes:
            if num%p == 0:
                factors.add(p)
                num //= p
                break
    return factors


def has_n_distinct_factors(arr,primes):
    #  primes is arr of primes less than num
    #  arr = [n1,n2,n3...]
    n = len(arr)
    # total_factors = n*n
    all_factors = set()
    for num in arr:
        f = prime_factors(num,primes)
        if len(f) != n: return False
        all_factors=all_factors.union(f)

    return True


found = False
i = 3
n = 4
primes = [2]
while not found:
    if is_prime(i,primes):
        primes.append(i)
        continue
    arr = list(range(i,i-n,-1))
    # arr = [i,i-1]
    if has_n_distinct_factors(arr,primes):
        print(arr)
        found = True
    i+=1

#  134043 correct
