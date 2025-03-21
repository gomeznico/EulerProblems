"""
10! is 10x9x8x7...x3x2x1 = 3628800

the sum of the digits of 10! = 27 = 3+6+2+8+8+0+0

what is the sum of the digits of 100!

"""

num = 1
for i in range(1,101):
    num*=i
ans=0
for c in str(num):
    ans += int(c)
print(ans)
