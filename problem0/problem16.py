"""
2^15 is 32768
the sum of its digits are -> 3+2+7+6+8 = 26


what is the sum of digits for 2^1000
"""

# for i in range(20):
num = str(pow(2,1000))
sum = 0
for c in num: sum += int(c)
print(sum)
