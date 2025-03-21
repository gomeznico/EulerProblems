"""
Problem 56

A googol (10^{100}) is a massive number: one followed by one-hundred zeros; 100^{100} is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
"""
print(100**100)

def digital_sum(num):
    s = str(num)
    sum = 0
    for c in s: sum+= int(c)
    return sum

max_sum = 0
for a in range(1,100):
    for b in range(1,100):
        num = a**b
        max_sum = max(max_sum, digital_sum(num))

print(max_sum)
