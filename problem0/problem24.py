"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math
## get all permuations
## sort
## get millionth index

def get_permutations(arr):
    if len(arr) <2:
        return [arr]
    first = arr[0]
    perms = get_permutations(arr[1:])
    ans = []
    for perm in perms:
        for i in range(len(perm)+1):
            new = perm[0:i] + [first] + perm[i:]
            ans.append(new)
    return ans

# perms = get_permutations([0,1,2,3,4,5,6,7,8,9])
# perms = get_permutations([0,1,2])
# perms.sort()
# print(str(perms[999999]))


## in lexographic order, the first 9! = 362,880 must start with 0
## the next 9! must start with 1, then 2...

numbers = [0,1,2,3,4,5,6,7,8,9]
chosen_index = 1000000-1
# chosen_index = 1
permutation = ['']*len(numbers)
for i in range(len(permutation)):
    spaces_left = len(numbers)-1
    digit_possibilities = math.factorial(spaces_left)

    ind_number = chosen_index // digit_possibilities
    
    permutation[i] = numbers[ind_number]
    numbers = numbers[0:ind_number]+numbers[ind_number+1:]
    chosen_index -= ind_number*digit_possibilities

print(permutation)



