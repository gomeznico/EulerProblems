"""
By listing the first six prime numbers:2,3,5,7,11,13 we can see that the
6th prime is 13

What is the
10,001 st prime number?
"""
import math
primes = [2,3,4,5,6,7,11,13]
def is_prime(num):
    if num%2 ==0: return False
    div=3
    while div <= math.sqrt(num):
        if num%div == 0: return False
        else: div+=2
    return True

def nth_prime(n):
    primes =[2]
    num = 3
    while len(primes) < n:
        if is_prime(num): primes.append(num)
        num +=1
    return primes[-1]

print(nth_prime(1))
print(nth_prime(2))
print(nth_prime(3))
print(nth_prime(4))
print(nth_prime(5))
print(nth_prime(100))
print(nth_prime(500))
print(nth_prime(1000))
print(nth_prime(5000))
print(nth_prime(10000))
print(nth_prime(10001))

