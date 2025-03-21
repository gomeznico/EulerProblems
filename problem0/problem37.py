"""
3797 is interesting.  it is prime, but so are all of its truncations
3797
 797
  97
   7

it also works frm the other end
3797
379
37
3

there are only 11 primes like this
what is there sum

2,3,5,7 are not considered truncatable


"""
## build up primes
import math
def is_prime(n):
    if n == 2: return True
    if n%2 ==0 or n==1: return False
    i=3
    while i<= math.sqrt(n):
        if n%i == 0: return False
        i +=2
    return True


## brute force:
# primes = set()
# for i in range(2,1000000):
#     if is_prime(i): primes.add(i)

def is_truncatable(num):
    if num in [2,3,5,7] or not is_prime(num): return False
    num_str = str(num)
    for i in range(1,len(num_str)):
        f = int(num_str[0:0-i])
        b = int(num_str[i:])
        if not is_prime(f) or not is_prime(b): return False
    return True

print(is_truncatable(3797))

# truncatables =[]
# for n in primes:
#     if is_truncatable(n): truncatables.append(n)

# print(truncatables)
# print(sum(truncatables))


## smarter approach
## first digit must be one of the primes, 2,3,5,7 to make truncating from right possible
## digits after first cannot be 2,4,5,6,8 since they will make the number not prime when right trunc.
## allowable digits after first 1,3,7,9
## last digit must be 3,7 as 9 and 1 are not primes when truncated from left
## [2,3,5,7] - - - ... - [3,7]

first_digit_primes = '2357'
middle_digits ='1379'
last_digit = '37'

def combinations(len,choices):
    ans = []
    if len == 1:
        for i in choices:
            ans.append(i)
    else:
        perms = combinations(len-1,choices)
        for perm in perms:
            for i in choices:
                ans.append(i+perm)
    return ans

truncatables = set()

# 2 digit primes
for first in first_digit_primes:
    for last in last_digit:
        num = int(first+last)
        if is_truncatable(num): truncatables.add(num)
print(truncatables)

# larger digit primes
num_length = 3
while len(truncatables)<11:
    # get all combos of middle segment
    middle_len = num_length-2
    middles = combinations(middle_len,middle_digits)
    for first in first_digit_primes:
        for middle in middles:
            for last in last_digit:
                num = int(first+middle+last)
                if is_truncatable(num):
                    truncatables.add(num)
                    print(truncatables)
    num_length+=1

print(truncatables)
print(sum(truncatables))

















