"""
the numebr 197 is called circular prime becasue all rotations of the digits are themselves prime

197, 971, 719

there are 13 such primes below 100
2,3,5,7,11,13,17,31,37,71,73,79,97

how many circular primes are below 1million
"""

import math, time
primes = set([2])
circular = set()
def is_prime(n):
    if n == 2: return True
    elif n%2 == 0: return False
    i = 3
    while i <=math.sqrt(n):
        if n%i == 0: return False
        i+=2
    return True

def is_circular(n):
    ## n is prime
    s = str(n)
    rotations = set()
    for i in range(len(s)):
        rotation = int(s[i:]+s[0:i])
        rotations.add(rotation)
        if not is_prime(rotation): return False
    return rotations


max = 1000000

start = time.time()
for i in range(2,max):
    if i in circular: continue
    if is_circular(i):
        circular.update(is_circular(i))
end = time.time()
print('slow time = ',end-start)
print(circular)
print(len(circular))

