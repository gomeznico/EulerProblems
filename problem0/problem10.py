"""
the sum of primes below 10 is
2+3+5+7 =17

find the sum of all primes below 10million

"""
import math

def isPrime(num):
    if num%2 == 0:  return False
    div=3
    while div < math.sqrt(num)+1:
        if num%div == 0:  return False
        div+=2 # only chek odd divisors
    return True

def arr_of_primes(max_val_prime):
    primes =[2]
    num = primes[-1]
    while num < max_val_prime:
        if isPrime(num): primes.append(num)
        num+=1
    print(len(primes))
    ans = sum(primes)
    return ans

print(arr_of_primes(2000000))
