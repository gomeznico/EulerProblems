"""
Problem 66

Consider quadratic Diophantine equations of the form:
x^2 - Dy^2 = 1
For example, when D=13, the minimal solution in x is 649^2 - 13 * 180^2 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 - 2 * 2^2 = 1
2^2 - 3 * 1^2 = 1
{color{red}{mathbf 9}}^2 - 5 * 4^2 = 1
5^2 - 6 * 2^2 = 1
8^2 - 7 * 3^2 = 1

Hence, by considering minimal solutions in x for D le 7, the largest x is obtained when D=5.
Find the value of D le 1000 in minimal solutions of x for which the largest value of x is obtained.
"""
from math import sqrt,gcd
# x =1
# y =1
# x*x - D*y*y = 1
# x*x - 1 = D*y*y
# (xx - 1)/D = yy
# sqrt(term) = y

def sqrt_expansion(n):
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

        r = len(arr)

    return first_term, arr

def get_convergence_fractions(first_term,arr):
    r = len(arr)-1
    # ensure last term is correct term to get
    if r%2 == 0:
        arr = arr+arr[0:-1]
        # if r is even, get term @ 2*r + 1
    else: arr =arr[0:-1]
        # if r is odd, get term @ r

    fractions = []
    ## go in reverse
    for i,a in enumerate(arr):
        num = 1
        den = a

        k = i-1
        while k>=0:
            b = arr[k]
            # b + num/den => b*den + num / den
            num = (den*b)+num
            den = den

            #flip in prep for next addition
            num, den = den, num
            k+= -1

        frac = (num,den)
        fractions.append(frac)

    # add first term to fractions to create improper fractions
    out =[first_term]
    for num,den in fractions:
        num = num + (den*first_term)
        d = gcd(num,den)
        num //= d
        den //= d
        # simplify num/den
        f = (num,den)
        out.append(f)
    return out

def solve_for_x(D):
    first_term, arr = sqrt_expansion(D)
    convergents = get_convergence_fractions(first_term,arr)
    num,den = convergents[-1]
    print(f'For D={D}, minimized x={num}')
    return num

max_x = 0
max_D = 0
limit = 1000
for D in range(2,limit+1):

    if sqrt(D)%1==0: continue
    # if D%10==0: print(D)
    x = solve_for_x(D)
    if x>max_x:
        max_x,max_D = x,D
print(f'Maximum x is when D = {max_D}, for an x val of: {max_x}')


