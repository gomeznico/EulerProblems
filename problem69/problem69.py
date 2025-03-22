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

primes = [2]
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

# generate primes up to 1_mill
for i in range(3,1_000_000):
    if is_prime(i,primes):
        primes.append(i)

primes_set=set(primes)
print(prime_factors(12,primes))

def phi(n):
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

val = 0
ans = 0
limit= 1_000_000
start = time.time()
for n in range(2,limit+1):
    phi_val = phi(n)
    if n/phi_val>val:
        ans,val = n, n/phi_val
end = time.time()
print(f'going through {limit:_} values took {end-start:.4f} seconds')
print(f'n val of {ans} results in highest n/phi = {val}')

# 1_000 vals->  0.0016 sec
# 10_000 vals-> 0.0363 sec
# 100_000 vals> 1.5551 sec
# 1_000_000vals> 92.55 sec
# ans n=510510 , n/phi(n) = 5.539...



