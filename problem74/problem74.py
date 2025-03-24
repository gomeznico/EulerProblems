"""
Problem 74

The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
1! + 4! + 5! = 1 + 24 + 120 = 145.
Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 to 363601 to 1454 to 169
871 to 45361 to 871
872 to 45362 to 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 to 363600 to 1454 to 169 to 363601 (to 1454)
&78 to 45360 to 871 to 45361 (to 871)
&540 to 145 (to 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""
import time
from math import factorial

def step(num):
    digits = [ int(c) for c in list(str(num))]
    return sum([factorial(d) for d in digits])

def get_chain(num):
    c = [num]
    while step(num) not in c:
        num = step(num)
        c.append(num)
    return c

def solve_BF(limit):
    s = time.time()
    len_of_chain = {}
    count_60 = 0
    for n in range(1,limit+1):
        num = step(n)
        chain = [n]
        while num not in chain:
            chain.append(num)
            num = step(num)
        len_of_chain[n] = len(chain)
        if len(chain)==60: count_60+=1
    e = time.time()
    print(f'checked numbers up to {limit:_} took {e-s:.4} sec. ans = {count_60}')

    # print(len(len_of_chain))
    ##filtered
    # out = []
    # print(len(len_of_chain.values()))
    # for n in len_of_chain:
    #     if len_of_chain[n] == 60:
    #         out.append(n)
    # print(len(out))
    # return out

def solve_V2(limit):
    s = time.time()
    len_of_chain = {}
    count_60 = 0
    for n in range(1,limit+1):
        # if n == 1497:
        #     print(n)

        if n in len_of_chain: continue


        num = step(n)
        chain = [n]

        #build chain until it loops or known num found
        while num not in chain and num not in len_of_chain:
            chain.append(num)
            num = step(num)

        # if known loop found
        if num in len_of_chain:
            to_add = len_of_chain[num]
            for i,start in enumerate(chain):
                val = len(chain)-(i) + to_add
                len_of_chain[start] = val
                if val==60: count_60+=1

        ## new complete loop found
        elif num == chain[0]:
            ## add all nums in chain to
            for start in chain:
                len_of_chain[start] = len(chain)
                if len(chain)==60: count_60+=1

        ## new complete loop found + pre-loop found
        else:
            ## num is the repeated number, and thus start of the new loop
            ## comlete loop
            i = chain.index(num)
            loop = chain[i:]
            for start in loop:
                len_of_chain[start] = len(loop)
                if len(loop)==60: count_60+=1

            ##pre-loop
            pre_loop = chain[0:i]
            to_add = len(loop)
            for i,start in enumerate(pre_loop):
                val = len(pre_loop)-(i) + to_add
                len_of_chain[start] = val
                if val==60: count_60+=1

    e = time.time()
    print(f'checked numbers up to {limit:_} took {e-s:.4} sec. ans = {count_60}')

    # print(len(len_of_chain))
    ## filtered
    # chains_of_60 = []
    # print(len(len_of_chain.values()))
    # for n in len_of_chain:
    #     if len_of_chain[n] == 60:
    #         chains_of_60.append(n)
    # print(len(chains_of_60))
    # return chains_of_60

limit = 1_00
solve_BF(limit)
# checking numbers up to 1000 took 0.0284 sec. ans = 0
# checking numbers up to 10_000 took 0.3441 sec. ans = 42
# checking numbers up to 100_000 took 3.689 sec. ans = 42
# checking numbers up to 1_000_000 took 34.44 sec. ans = 402

solve_V2(limit)
# checked numbers up to 1_000 took 0.001632 sec. ans = 0
# checked numbers up to 10_000 took 0.0129 sec. ans = 42
# checked numbers up to 100_000 took 0.1358 sec. ans = 42
# checked numbers up to 1_000_000 took 1.523 sec. ans = 402
