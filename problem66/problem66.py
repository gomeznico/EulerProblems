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


