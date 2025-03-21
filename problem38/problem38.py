"""
Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3).
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def concatinated_product(num,arr):
    out = []
    for n in arr:
        out.append(str(num*n))
    return int(''.join(out))

def is_pandigital(num):
    s = str(num)
    s_ordered = ''.join(sorted(s))
    return s_ordered == '123456789'



a =1
b = [1,2,3,4,5,6,7,8,9]

s = concatinated_product(a,b)
print(is_pandigital(s))


# max possible i with min arr [1,2]-> 2 numbers, each must be 5 digits or less
# therfore, max i is 10,000.
# max length of arr is 1->9.  with i=1 => num = 123456789

max_pandigital = 0
for i in range(0,10_000):
    # if i%100_000 == 0: print(i)
    for n in range(2,9):
        arr = list(range(1,n))
        num = concatinated_product(i,arr)
        if is_pandigital(num):
            max_pandigital = max(max_pandigital,num)
            print('new max number:', max_pandigital,i,arr)

# 932718654

