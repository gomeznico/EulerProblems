"""
for a^b where 2 <= a,b <= 5

there are 16 total combinations
15 when tduplicates are removed


how many distinct terms are generated for
2 <= a,b <=100
"""

## brute force
nums = set()
for a in range(2,101):
    for b in range(2,101):
        num = pow(a,b)
        nums.add(num)
print(len(nums))
#  9183 for n = 100

