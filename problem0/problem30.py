"""
1634 = 1^4 6^4 3^4 4^4

8208 = 8^4 2^4 0^4 8^4

9474 =9^4 4^4 7^4 4^4

1634 + 8208 + 9474 = 19316

these are the only digits that can be wriiten as a sum of the 4th powers of tehir digits
find the sum of all numbers that can be written as the 5th poer of their digits
"""


def fifth_power_digits(num):
    n = str(num)
    digits = list(n)
    digits = [pow(int(x),5) for x in digits]
    return(sum(digits))

def fourth_power_digits(num):
    n = str(num)
    digits = list(n)
    digits = [pow(int(x),4) for x in digits]
    return(sum(digits))

fourth_pow_nums = []
for i in range(2,400000):
    if i == fourth_power_digits(i):
        fourth_pow_nums.append(i)

print(fourth_pow_nums)
print(sum(fourth_pow_nums))

fifth_pow_nums = []
for i in range(2,400000):
    if i == fifth_power_digits(i):
        fifth_pow_nums.append(i)
print(fifth_pow_nums)
print(sum(fifth_pow_nums))


