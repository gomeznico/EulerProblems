"""
Problem 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

#  there are 3 numbers of 4 digits each where
#  all are prime
#  they are permutaions of the same 4 digits
#  they incriment up in the same way


def is_prime(num,primes):
    if num ==2: return True
    for factor in primes:
        if num%factor == 0: return False
    return True

def is_permutations(arr):
    a = set()
    for n in arr:
        s =''.join(sorted(str(n)))
        a.add(s)
    return len(a) == 1


primes = [2]
four_digit=[]
n =3
while n < 10000:
    if is_prime(n,primes):
        primes.append(n)
        if len(str(n)) == 4: four_digit.append(n)
    n+=1

print(len(four_digit))
print(len(primes))

for i,a in enumerate(four_digit):
    if i%100 == 0: print(i)
    for j,b in enumerate(four_digit[i+1:]):
        for k,c in enumerate(four_digit[j+i+2:]):
            if c-b == b-a and is_permutations([a,b,c]):
                print([a,b,c])
                print(str(a)+str(b)+str(c))
# 296962999629

