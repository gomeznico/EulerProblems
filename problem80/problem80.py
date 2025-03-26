"""
Problem 80

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.
"""

# use sqrt expansion from problem 64
#  get cont fraction of each sqrt (n= [1,100])
#  use cont fraction to get convergents for each sqrt
from math import sqrt, gcd
import time


def decimal_exp_long_division(frac,n):
    #  get string of decimal fraction up to n decimal places
    ## known that num < den, so all ans start
    num,den = frac
    ans = ''
    quotient = num
    divisor = den
    while len(ans) < n:
        if quotient == 0:
            ans += '0'* (n - (len(ans)-2))
            break
        i = -1
        while quotient < divisor:
            quotient*= 10
            i+=1

        c = quotient//divisor
        remainder = quotient%divisor
        ans+= '0'*i + str(c)
        quotient=remainder

    return ans

def found_last(fractions,decimal_places):
    f1,f2 = fractions[-1],fractions[-2]
    f1_str = decimal_exp_long_division(f1,decimal_places+5)
    f2_str = decimal_exp_long_division(f2,decimal_places+5)

    return f1_str[0:decimal_places] == f2_str[0:decimal_places]

def sqrt_expansion(n):
    # from problem 64
    first_term = int(sqrt(n))
    arr = []
    # sqrt(n) = first_term + (sqrt(n) - a) / b
    a,b = first_term, 1

    # ensure loop by letting it repeat 10x
    check = 10
    while True:
        # flip and get whole term
        den = sqrt(n) - a
        num = b
        term = int(num/den)
        # print( f'{term} +   sqrt{n} - {a} / {b}')


        arr.append(term)
        if check*arr[0:len(arr)//check] == arr:
            arr = arr[0:len(arr)//check]
            break

        # get vals for next expansion, simplify a and b
        next_b = (n - a*a)
        a = term*next_b - b*a

        a/=b
        b=next_b/b

    return first_term, arr
    # print(arr)

def get_convergents(n,decimal_places):
    a, arr = sqrt_expansion(n)

    ## adapted from prob 65
    ## generate convergents untill diff of last two terms is less than 100 dec places
    convergents = []
    n = 1
    while n<=2 or not found_last(convergents, decimal_places):
        ## generate arr of k terms
        times = n//len(arr)
        remainder = n%len(arr)
        created_arr = arr*times + arr[0:remainder]

        num = 1
        den = created_arr[-1]
        k = len(created_arr)-2

        # while loop iterates through created_arr backwards until at start
        # constructs the final frac from smallest term to largest term
        while k>=0:
            b = created_arr[k]
            # b + num/den => b*den + num / den
            num = (den*b)+num
            den = den

            #flip in prep for next addition
            num, den = den, num
            k+= -1

        ## this is fraction using up to i terms
        frac = (num,den)
        convergents.append(frac)
        n+=1
    return a, convergents

def solve(limit):
    s = time.time()
    decimal_places = 100

    perfect_squares = [i*i for i in range(1,11)]
    checksum = 0

    for n in range(1,limit+1):
        if n in perfect_squares: continue

        a, convergents = get_convergents(n,decimal_places+5)
        f = decimal_exp_long_division(convergents[-1],decimal_places+5)
        # print(n, f)
        remaining_places = decimal_places - len(str(a))
        f = str(a) + f[0:remaining_places] # first 100 decimal places
        digital_sum = sum([int(d) for d in f])

        checksum+=digital_sum
    e = time.time()
    print(f"the digital sum for first 100 dig. of sqrt's up to {limit} is {checksum} found in {e-s:f} seconds")


solve(100)
# 40727 incorrect -> did not account for the first whole term in front of decimal
# the digital sum for first 100 dig. of sqrt's is 40886 found in 0.623047 seconds

