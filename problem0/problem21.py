"""
let d(n) be defined as the sum of proper divsors of n

if d(a) = b and d(b)=a, where a!= b, then a and b are an amicable pair, and they are called amicable numbers

for example
d(220) = 1,2,4,5,10,11,20,22,44,55,110 ==> d(220) = 284
d(284) = 1,2,4,71,142 ==> d(284) = 220

so 280 and 284 are amicable numbers

what is the sum of all amicable numbers below 10000
"""
import math
divisors_sum ={}

def divisors(num):
    divisors = set()
    i=1
    while i <= math.sqrt(num):
        if num%i == 0:
            divisors.add(int(num/i))
            divisors.add(i)
        i+=1
    divisors.discard(num)
    return divisors

def get_all_d(max_num):
    divisors_sum ={}
    for i in range(2,max_num+1):
        div = divisors(i)
        divisors_sum[i] = sum(div)
    return divisors_sum

d = get_all_d(10500)

amicable_nums = set()
for a in d:
    b = d[a]
    if b in d and d[b]==a and a!=b:
        amicable_nums.add(a)
        amicable_nums.add(b)
print(amicable_nums)
print(sum(amicable_nums))

