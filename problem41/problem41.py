"""
Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""
import math

def is_prime(num):
    if num in {1,2}: return True
    factor = 2
    max_factor = int(math.sqrt(num))
    while factor <=max_factor:
        if num%factor == 0: return False
        factor+=1
    return True

def create_n_pandigitals(n):
    if n ==2:
        return [21,12]
    else:
        arr = create_n_pandigitals(n-1)
        out = []
        for num in arr:
            s = list(str(num))
            for i in range(len(s)+1):
                inserted = ''.join(s[0:i] +[str(n)] + s[i:])
                out.append(int(inserted))
        return out

def all_pandigitals():
    out = []
    for n in range(2,10):
        out += create_n_pandigitals(n)
    return out


valid_answers=[]
for num in all_pandigitals():
    if is_prime(num):
        valid_answers.append(num)

# print(valid_answers)
print(max(valid_answers))
# 7652413 correct!

