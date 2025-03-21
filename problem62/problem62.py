"""
Problem 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
Find the smallest cube for which exactly five permutations of its digits are cube.
"""
import time
from collections import Counter as counts, defaultdict

# start = time.perf_counter()
# end = time.perf_counter()
# elapsed_time = end - start
# print(f"Elapsed time: {elapsed_time:0.4f} seconds")

def get_key(cube):
    digits = counts(str(cube))
    key = ['']*10
    for d in digits:
        key[int(d)] = int(digits[d])
    key = tuple(key)
    return key

def smallest_cube_with_n_perms(i):

    permutations = defaultdict(int)
    n = 1
    found = False
    while not found:
        # if n%1_000==0: print(n)
        cube = n*n*n
        key = get_key(cube)
        permutations[key]+= 1
        if permutations[key] == i:
            found = True
        n+=1

    # go thorugh cubes again until key matches
    n = 1
    while get_key(str(n*n*n)) != key:
        n+=1
    print(f'Smallest cube found with {i} permutations: {n}^3 = {n*n*n}')

smallest_cube_with_n_perms(3)
smallest_cube_with_n_perms(5)
