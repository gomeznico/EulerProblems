"""
Problem 57

It is possible to show that the square root of two can be expressed as an infinite continued fraction.
sqrt 2 = 1+ frac 1 {2+ frac 1 {2 +frac 1 {2+ ...}}}
By expanding this for the first four iterations, we get:
1 + frac 1 2 = frac  32 = 1.5
1 + frac 1 {2 + frac 1 2} = frac 7 5 = 1.4
1 + frac 1 {2 + frac 1 {2+frac 1 2}} = frac {17}{12} = 1.41666 ...
1 + frac 1 {2 + frac 1 {2+frac 1 {2+frac 1 2}}} = frac {41}{29} = 1.41379 ...
The next three expansions are frac {99}{70}, frac {239}{169}, and frac {577}{408}, but the eighth expansion, frac {1393}{985}, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.
In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
"""


# 2 + 1/2 = 5/4

def frac_iter(n):
    if n == 1: return 3,2

    num,den = 2,5
    n+=-1
    while n>1:
        num,den = step(num,den)
        n += -1

    # 1+ frac
    return num+den,den

def step(num,den):
    # output: 1 / (2 + frac)

    # 2 + frac =
    num = 2*den + num

    # 1 / new frac =
    num,den = den,num
    return num,den

count = 0
for n in range(1,1001):
    num,den = frac_iter(n)
    if len(str(num)) > len(str(den)): count +=1
print(count)
# 153 correct!

