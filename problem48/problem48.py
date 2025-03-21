"""
Problem 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^{10} = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^{1000}.
"""


## only need to keep adding/multiplying last 10 digits over and over

n = 5
num = 1
for _ in range(n):
    num*=n
print(num)

# 3^3 = 27              2 dig
# 9^9 = 3486784401      10 dig
# 10^10 =10000000000    11 dig
# 11^11 =285311670611   12 dig
# n=12   8916100448256  13 dig

def truncated_power(n):
    # return last 15 digits of resulting n^n
    digits = 11
    num = 1
    for _ in range(n):
        num*=n
        num =str(num)
        if len(num)>digits: num = num[-digits:]
        num = int(num)
    return num

print(truncated_power(n))


last_digits = 0
for i in range(1,1001):
    d = truncated_power(i)
    last_digits+=d
print(last_digits)

# 445127819110846700
# ...9110846700
