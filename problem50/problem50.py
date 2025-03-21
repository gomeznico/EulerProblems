"""
Problem 50

The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13.
This is the longest sum of consecutive primes that adds to a prime below one-hundred.
The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
import math

def is_prime(num,primes):
    if num ==2: return True
    for factor in primes:
        if factor > math.sqrt(num): break
        if num%factor == 0: return False
    return True

# num of primes below 1mil = ~78,000
## start with seq of sum of 1mil

n = 1_000_000
primes = [2]
i=3
while sum(primes) < n:
    if is_prime(i,primes):
        primes.append(i)
    i+=2

## check all possible windows within primes seq
i = 0
length = len(primes)
seq=primes[i:i+length]
max_length =0

while length!=0:
    # check longest sequences first, stop when one is found
    i = 0
    while i+length < len(primes):
        seq = primes[i:i+length]
        if is_prime(sum(seq),primes) and len(seq)>max_length:
            max_length = len(seq)
            print(sum(seq), length)
        i+=1
    length-=1







def can_be_written_consecutive(num,primes):
    # create sliding window
    i,j = 0,1
    window = sum(primes[i:j])
    while window != num:
        if window < num: j+=1
        if window > num: i+=1
        window = sum(primes[i:j])
        if primes[j]==num: break
    if window == num:
        return len(primes[i:j])
    return False

print(can_be_written_consecutive(41,primes))
print(can_be_written_consecutive(953,primes))
print(can_be_written_consecutive(997651,primes))    # 543
