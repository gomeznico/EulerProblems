"""
Problem 51

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""
# find smallest prime by which replacing some part of it with the same digit results in 7 other primes

import math

def is_prime(num,primes):
    if num ==2: return True
    for factor in primes:
        if factor > math.sqrt(num): break
        if num%factor == 0: return False
    return True

primes = [2]
n = 3
while n < 1_000_000:
    if is_prime(n,primes): primes.append(n)
    n+=2
primes_set = set(primes)

def get_permutation(length,n):
    # length is length of number, num digits
    # n is number of spots to replace

    # output is arr of sets of which coords to replace

    # base case, each set is single index
    if n==1:
        out = [set([i]) for i in range(length)]
        return out

    prev = get_permutation(length,n-1)
    out = []
    for a in prev:
        for i in range(length):
            b = a.copy()
            b.add(i)
            # print(b, len(b))
            if len(b) == n and b not in out:
                out.append(b)
    return out

def replace_n_digits(n,num):
    s = list(str(num))
    families = {}
    arr = get_permutation(len(s),n)

    for a in arr:
        base = s[::]
        for i in a:
            base[i] = '*'
        base = ''.join(base)
        families[base] = []

        for c in '0123456789':
            copy=base[::]
            copy = copy.replace('*',c)
            if int(copy) in primes_set and copy[0]!='0':
                families[base].append(copy)
    return families

def largest_family(num):
    num_digits = len(str(num))
    families = {}
    for n in range(1,num_digits):
        families.update(replace_n_digits(n,num))

    # return largest family size and key
    key = max(families, key = lambda x:len(families[x]))
    return [key,families[key]]

def find_prime_family_size(family_size):
    # start with 2-digit primes
    for num in primes[4:]:
        key,family = largest_family(num)
        if len(family) == family_size:
            print(key, family)
            break

find_prime_family_size(5)  # *1 ['11', '31', '41', '61', '71']
find_prime_family_size(6)  # *3 ['13', '23', '43', '53', '73', '83']
find_prime_family_size(7)  # 56**3 ['56003', '56113', '56333', '56443', '56663', '56773', '56993']
find_prime_family_size(8)  # *2*3*3 ['121313', '222323', '323333', '424343', '525353', '626363', '828383', '929393']


