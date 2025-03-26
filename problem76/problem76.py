"""
Problem 76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""
import time
# Theory:
# f(n) = g(n,1) + g(n,2) + ...g(n, n-1)
# g(n,1) = 1        combo of {1,1,1,...} n instances of 1
# g(n,n-1) = 1      combo of {n-1, 1}
# g(n,2) = n//2     combo of {2,1,1,..}, {2,2,1,1...}, {2,2,2,1...} etc.
# g(n, x) where n-x == x+1 => return f(n-x)
# x<n/2 ,   g(n,x) = g(n-x,1) + g(n-x,2) + ... g(n-x,x)   ex: g(8,3) = g(5,1) + g(5,2) + g(5,3)
# x>= n/2 , g(n,x) = f(n-x) + 1                           ex: g(8,5) = f(3) +




def count_combos(n,memo={}):
    if n in memo: return memo[n]
    sum = 0
    for i in range(1,n):
        sum+=count_combos_with_ints_lessthan(n,i,memo)
    memo[n] = sum
    return memo[n]

def count_combos_with_ints_lessthan(n,x, memo={}):
    # count ways to sum to n, starting with int x and all ints less than x
    if (n,x) in memo: return memo[(n,x)]
    if x == 1 or x == n-1: return 1

    elif x == 2:
        memo[(n,x)] = n//2
    elif n-x == x+1:
        memo[(n,x)] = count_combos(n-x)

    elif x < n/2:
        sum = 0
        for i in range(1,x+1):
            sum+=count_combos_with_ints_lessthan(n-x,i,memo)
        memo[(n,x)] = sum
    elif x >= n/2:
        memo[(n,x)] = count_combos(n-x)+1

    return memo[(n,x)]


def possible_sums_BF(n,memo={}):
    if n == 1: return set([(1,)])
    if n == 2: return set([(1,1)])
    if n in memo: return memo[n]

    combos = set()
    for i in range(1,n):
        prev_combos = possible_sums_BF(i,memo)
        diff = n-i
        new = [tuple(sorted(list(c) +[diff])) for c in prev_combos]
        combos.update(new)
        # add (i, n-i)
        combos.add(tuple(sorted([i,diff])))

    memo[n] = combos
    return combos

n = 100
s = time.time()
# l = possible_sums(n)
print(count_combos(n))
# for _ in l: print(_)
e = time.time()
print(f'found {count_combos(n)} combinations for integers that add to {n}, in {e-s:.2f} seconds' )

