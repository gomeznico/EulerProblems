"""
Problem 63

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
"""
# go through all possible, n powers unitl not n digits anymore

# for n = 1-> 1,2,3,4,5,6,7,8,9 xx
# for n = 2-> 16, 25,36...81
# ...

# for n=26-> 1^26 is 1, 2^26 is 67108864, 3^26->254186580000000
# ...
# at some point, an n will have no possible outputs that are n-digits long.  assume that is limit

total = 0
n = 1
while True:
    count = 0
    c = 1
    while True:
        num = pow(c,n)
        if len(str(num)) == n:
            count +=1
        if len(str(num)) > n:
            break
        c+=1
    print(f'num integers for n = {n:<.2f} : {count}')
    total+=count
    if count == 0: break
    n+=1
print(total)
