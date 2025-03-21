"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1+2+4+7+14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1+2+3+4+6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
 By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math
def divisors(num):
    div = set()
    i = 1
    while i <= math.sqrt(num):
        if num%i == 0:
            div.add(i)
            div.add(num//i)
        i+=1
    div.discard(num)
    return div

def is_abundant(num):
    div = divisors(num)
    if sum(div) > num: return True
    return False

abundant_nums = []  #length is 6962 nums
for i in range(30000):
    if is_abundant(i): abundant_nums.append(i)
abundant_nums_set = set(abundant_nums)

def can_be_written(num):
    for n1 in abundant_nums:
        n2 = num-n1
        if n2 in abundant_nums_set: return True
        if n2 < 0: break
    return False

sum = 0
for i in range(0,30000):
    if not can_be_written(i): sum +=i
print(sum) # 4179871


