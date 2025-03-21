"""
Problem 46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
## composite numbers are nums with more than 2 factors (not prime)
# 1 is neither prime nor composite

import math
def is_odd_composite(num,primes):
    return not is_prime(num,primes)

def is_prime(num,primes):
    if num ==2: return True
    for factor in primes:
        if num%factor == 0: return False
    return True

def follows_conjecture(num, primes):
    # assume num is odd and composite already
    # num = prime + 2*a*a
    for p in primes:
        a = math.sqrt((num-p)/2)
        if a == int(a): return True
    return False

found = False
primes = [2]
num = 3
while not found:
    if is_prime(num,primes):
        primes.append(num)
    if not follows_conjecture(num,primes):
        print(num)
        break
    num +=2

# 5777 correct!
