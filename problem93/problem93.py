"""
Problem 93

By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, -, *, /) and brackets/parentheses, it is possible to form different positive integer targets.
For example,

8 = (4 * (1 + 3)) / 2
14 = 4 * (3 + 1 / 2)
19 = 4 * (2 + 3) - 1
36 = 3 * 4 * (2 + 1)

Note that concatenations of the digits, like 12 + 34, are not allowed.
Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.

Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.
"""

"""
{1,2,3,4}
-> 31 different numbers possible
-> theres a streak of num from 1->28 inclusive
"""
import time
from itertools import combinations, permutations, product
## Brute Force:
# for each a,b,c,d
# combos of a,b,c,d => 10 pick 4 => 210 sets to check ->
#   each set has 24 perms
#   four operaters in 3 spots -> 64 permutations
#   paranthesis options = 10 (27)
#
#   -> 24*64*27 = 41,472 possibilities ... per a,b,c,d
#   total = 8_709_120 possibilities


count = 0
digits = [0,1,2,3,4,5,6,7,8,9]
for _ in combinations(digits,4):
    count+=1
print(count)


# ops = ['*','/','+','-']
# for _ in product(ops,repeat=3):
#     print(_)



"""
terms :     priority of adj pairs.  num of parenth around that pair

a b c d     0,0,0
(a b)c d    1,0,0
(a b c)d    1,1,0
 a(b c)d    0,1,0
 a(b c d)   0,1,1
 a b(c d)   0,0,1

(a b)(c d)  1,0,1 <-

(a(b c)) d  1,2,0
((a b) c) d 2,1,0

a ((b c) d) 0,2,1
a ( b(c d)) 0,1,2

"""

def evaluate_expression(digits, operators, parenth):
    #create hierachy...
    # PEMDAS
    #find inner most parenth

    new_digits = digits[::]
    new_operators = operators[::]
    new_parenth = parenth[::]

    while len(new_digits) != 1:
        ## find first streak of terms in max priority/innermost parenth.
        max_pri = max(new_parenth)
        streak = 0
        for i in range(len(new_parenth)):
            pri = new_parenth[i]
            if pri == max_pri:
                streak +=1
            if pri != max_pri and streak>0:
                # streak has ended
                i += -1
                break

        start = i+1-streak
        end = i
        # inputs to evaluate terms in parentheses
        p_digits = new_digits[start:end+2]
        p_operators = new_operators[start:end+1]
        # p_parenth = new_parenth[start:end+1]

        num = eval_terms_in_parenth(p_digits,p_operators)
        if num is None: return None

        new_digits = new_digits[0:start] + [num] + new_digits[end+2:]
        new_operators = new_operators[0:start] + new_operators[end+1:]
        new_parenth = new_parenth[0:start] + new_parenth[end+1:]

    # all nested parenth. evaluated.  only 1 digit left
    return new_digits[0]

def eval_terms_in_parenth(digits,operators):

    pair_priorities = [1]*len(operators)
    for i,o in enumerate(operators):
        pair = (digits[i],digits[i+1])
        if o in {'+','-'}:
            continue
        if o in {'*','/'}:
            pair_priorities[i]+=1

    new_digits = digits[::]
    new_operators = operators[::]
    new_priorities = pair_priorities[::]

    while len(new_digits) != 1:
        ## find first pair at max priority
        max_pri = max(new_priorities)
        for i in range(len(new_operators)):
            a , b  = new_digits[i], new_digits[i+1]
            pri = new_priorities[i]
            op = new_operators[i]

            if pri == max_pri:
                ##evaluate pair
                pair = (a,b)
                num = evaluate_pair(pair,op)
                if num is None: return None

                ## adjust arrs to eval next pair
                new_digits = new_digits[0:i] +[num]+ new_digits[i+2:]
                new_operators = new_operators[0:i] + new_operators[i+1:]
                new_priorities = new_priorities[0:i] + new_priorities[i+1:]
                break
    return new_digits[0]

def evaluate_pair(pair,op):
    a,b = pair
    if op == '-':
        return float(a)-float(b)
    elif op == '+':
        return float(a)+float(b)
    elif op == '*':
        return float(a)*float(b)
    elif op == '/' and b!=0:
        return float(a)/float(b)
    if b == 0:
        return None

def solve(n:int):
    s = time.time()

    best_set = (0,0,0,0)
    best_streak = 0

    ops = '*+-/'
    ops_perms = list(product(ops,repeat=n-1))
    parenth_tiers = list(range(n-1))
    parenth_perms = list(product(parenth_tiers,repeat=n-1))
    digits = [0,1,2,3,4,5,6,7,8,9]

    parenth_possibilities = [
    [0,0,0],
    [1,0,0],
    [1,1,0],
    [0,1,0],
    [0,1,1],
    [0,0,1],
    [1,0,1],
    [1,2,0],
    [2,1,0],
    [0,1,2],
    [0,2,1]
]

    checked = 0
    total_combos_calcd = 0
    for nums_set in combinations(digits,n):   # 210 sets of a,b,c,d
        checked+=1
        if checked%10 == 0: print(f'{checked} sets checked of 210')

        results = set()
        for nums_perm in permutations(nums_set,n):    # 24 orderings of a,b,c,d
            for ops_perm in ops_perms:          # 64 permutations of * / + -
                for parenth in parenth_perms:   # 27 combos of 3 parenth
                # for parenth in parenth_possibilities:   # 11 possibilities
                    num = evaluate_expression(list(nums_perm), list(ops_perm), list(parenth))
                    total_combos_calcd +=1
                    if num is not None and num == int(num):
                        results.add(int(num))

        results = [0]+sorted([a for a in results if a>0])
        ## find streak,
        i = 0
        for i,number in enumerate(results):
            if i!=number:
                break
        streak = i-1
        if streak > best_streak:
            best_streak, best_set = streak, nums_set


    best_set = sorted(best_set)
    e = time.time()

    print(f'longest streak found is {best_streak} with set {best_set}.  {e-s:f} seconds elapsed')
    print(f'Total iterations followed {total_combos_calcd:_}')

# solve(4)
# 1258
# longest streak found is 51 with set [1, 2, 5, 8].  52.900923 seconds elapsed
# Total iterations followed 8_709_120

## Method2:
"""
instead of evaluating every nested version parenthesis, just check every order of evaluating pairs of digits
4 terms a,b,c,d
-> ab  bc  dc first ->
-> simplifies to arr of 3 terms:
x,y,z
-> xy yz
simplifies to 2 term array
-> 6 possible orderings of doing pairs of numbers per order of permutation of abcd and operators
 use recursion
 """


def evaluateV2(digits, operations):
    ## base case:
    if len(digits) == 2:
        return [evaluate_pair(digits,operations[0])]
        ## get number back

    ## get each possible pair
    vals = []
    for i in range(len(operations)):
        # evaluate pair
        # create new arr of digits and ops
        pair = digits[i:i+2]
        op = operations[i]
        num = evaluate_pair(pair,op)
        new_digits = digits[0:i] + [num] + digits[i+2:]
        new_ops = operations[0:i] + operations[i+1:]
        if num is None:
            vals += [None]
        else:
            vals += evaluateV2(new_digits,new_ops)
    return vals

def solveV2(n):
    s = time.time()

    best_set = (0,0,0,0)
    best_streak = 0

    ops = '*+-/'
    ops_perms = list(product(ops,repeat=n-1))
    digits = [0,1,2,3,4,5,6,7,8,9]

    checked = 0
    total_combos_calcd = 0
    for nums_set in combinations(digits,n):   # 210 sets of a,b,c,d
        checked+=1
        if checked%10 == 0: print(f'{checked} sets checked of 210')

        results = set()
        for nums_perm in permutations(nums_set,n):    # 24 orderings of a,b,c,d
            for ops_perm in ops_perms:                # 64 permutations of * / + -
                    vals = \
                        evaluateV2(list(nums_perm), list(ops_perm))
                    total_combos_calcd += len(vals)
                    for num in vals:
                        if num is not None and num == int(num) and num>0:
                            results.add(int(num))

        results = [0]+sorted(results)
        ## find streak,
        i = 0
        for i,number in enumerate(results):
            if i!=number:
                break
        streak = i-1
        if streak > best_streak:
            best_streak, best_set = streak, nums_set


    best_set = sorted(best_set)
    e = time.time()
    print(f'longest streak found is {best_streak} with set {best_set}.  {e-s:f} seconds elapsed')
    print(f'Total iterations followed {total_combos_calcd:_}')

solveV2(4)
# much much faster ~20x
# longest streak found is 51 with set [1, 2, 5, 8].  2.440840 seconds elapsed
# Total iterations followed 1_911_168

# testing with n=5 terms arranged:
# longest streak found is 192 with set [4, 5, 6, 7, 8].  245.687630 seconds elapsed
# Total iterations followed 179_746_560
