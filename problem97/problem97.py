"""
Problem 97

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 2^{6972593} - 1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p - 1, have been found which contain more digits.
However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433 * 2^{7830457} + 1.
Find the last ten digits of this prime number.
"""
import time
## 28433 * 2^{7830457} + 1

def last_x_digits_2_exp_n(x,n):
    num = 1
    num_digits = x+1
    for i in range(1,n+1):
        num *= 2
        if len(str(num)) > num_digits:
            num = str(num)[-num_digits:]
            num = int(num)

    return num


s = time.time()
power = 7830457
a = 28433
num = (a * last_x_digits_2_exp_n(10,power))+1
e = time.time()
print(f"Last 10 digits are {str(num)[-10:]} found in {e-s:f} seconds")
# Last 10 digits are 8739992577 found in 2.041162 seconds
