"""
the decimal numeber 585 can be written as 1001001001 in binary
it is palindromic in both bases (base 10, base 2)

find the um of all numebrs less than 1mill that are palind in both base 10 and base 2
"""

# 1000000 ~ 2^10*2^10

def base10_tobase2(num):
    ## with max 1million, max digit is 2^19
    binary = ''
    for i in range(19,-1,-1):
        n= pow(2,i)
        bin_digit = str(num//n)
        num = num%n
        binary = binary+bin_digit
    return binary

def is_pal(str):
    rev = str[::-1]
    return rev == str


pals = []
for i in range(0,1000000):
    binary = base10_tobase2(i).lstrip('0')
    num_str = str(i)
    if is_pal(num_str) and is_pal(binary): pals.append(i)

print(pals)
print(len(pals))
print(sum(pals))






