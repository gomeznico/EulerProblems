"""
n*n + n + 41

this eq will produce 40 primes for n->[0,39]
but n=10 and n=41 do not prpoduce primes

n*n - 79n + 1601 is another, whihc makes 80 primes, for n-> [0,79]
the product of the coeff = -79*1601 = -126479

consider n*n + an +b where -1000 < a < 1000 and -1000 <= b <= 1000

find the product of coeff a and b that produce the maximum amount of primes
for consecutive values of n
"""
import math

def is_prime(num):
    i = 2
    if num <1: return False
    while i <= math.sqrt(num):
        if num%i == 0: return False
        i+=1
    return True

def evaluate_eq(a,b,n):
    ans = n*n + a*n + b
    return ans


maximum = (0,0,-1000,-1000)
for a in range(-1000,1001):
    for b in range(-1000,1001):
        num, n = 1, -1
        while is_prime(num):
            n +=1
            num = evaluate_eq(a,b,n)
        if n > maximum[0]:
            maximum = (n,a*b,a,b)
            print(maximum)


