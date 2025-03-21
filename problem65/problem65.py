"""
Problem 65

The square root of 2 can be written as an infinite continued fraction.
sqrt{2} = 1 + dfrac{1}{2 + dfrac{1}{2 + dfrac{1}{2 + dfrac{1}{2 + ...}}}}
The infinite continued fraction can be written, sqrt{2} = [1; (2)], (2) indicates that 2 repeats ad infinitum. In a similar way, sqrt{23} = [4; (1, 3, 1, 8)].
It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for sqrt{2}.

&1 + dfrac{1}{2} = dfrac{3}{2}
&1 + dfrac{1}{2 + dfrac{1}{2}} = dfrac{7}{5}
&1 + dfrac{1}{2 + dfrac{1}{2 + dfrac{1}{2}}} = dfrac{17}{12}
&1 + dfrac{1}{2 + dfrac{1}{2 + dfrac{1}{2 + dfrac{1}{2}}}} = dfrac{41}{29}

Hence the sequence of the first ten convergents for sqrt{2} are:
1, dfrac{3}{2}, dfrac{7}{5}, dfrac{17}{12}, dfrac{41}{29}, dfrac{99}{70}, dfrac{239}{169}, dfrac{577}{408}, dfrac{1393}{985}, dfrac{3363}{2378}, ...
What is most surprising is that the important mathematical constant,e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ... , 1, 2k, 1, ...].
The first ten terms in the sequence of convergents for e are:
2, 3, dfrac{8}{3}, dfrac{11}{4}, dfrac{19}{7}, dfrac{87}{32}, dfrac{106}{39}, dfrac{193}{71}, dfrac{1264}{465}, dfrac{1457}{536}, ...
The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""
from math import sqrt, gcd

def get_convergence_fractions(first_term,arr):

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


first_term = 2
continued_fraction_arr = []
# create array for constant e
n = 1
chosen_term = 100
while len(continued_fraction_arr)<chosen_term-1:
    continued_fraction_arr += [1,2*n,1]
    n+=1
continued_fraction_arr = continued_fraction_arr[0:chosen_term-1]
fractions = get_convergence_fractions(first_term,continued_fraction_arr)

num,den = fractions[-1]
checksum = sum([int(c) for c in str(num)])
print(checksum)







