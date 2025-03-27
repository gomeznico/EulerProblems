"""
Problem 43

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. In this way, we note the following:
d_2*d_3*d_4 = 406 is divisible by 2
d_3*d_4*d_5 = 063 is divisible by 3
d_4*d_5*d_6 = 635 is divisible by 5
d_5*d_6*d_7 = 357 is divisible by 7
d_6*d_7*d_8 = 572 is divisible by 11
d_7*d_8*d_9 = 728 is divisible by 13
d_8*d_9*d_{10} = 289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

"""
def create_n_pandigital(n):
    if n==1:
        return ['01','10']
    arr = create_n_pandigital(n-1)
    out = []
    for s in arr:
        length = len(s)
        for i in range(length+1):
            new = s[0:i] + str(n) + s[i:]
            out.append(new)
    return out

def has_subdiv_prop(num:str):
    factors = [2,3,5,7,11,13,17]
    for i in range(1,8):
        pan = int(num[i:i+3])
        factor = factors[i-1]
        if pan%factor != 0: return False
    return True

arr = create_n_pandigital(9)
checksum = 0
for num in arr:
    if  num[0] != '0'and has_subdiv_prop(num):
        print(num)
        checksum+=int(num)
print(checksum)
# 16695334890
