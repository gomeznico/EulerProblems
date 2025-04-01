"""
Problem 95

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:
12496 to 14288 to 15472 to 14536 to 14264 (to 12496 to ...)

Since this chain returns to its starting point, it is called an amicable chain.
Find the smallest member of the longest amicable chain with no element exceeding one million.
"""
import math,time

def get_divisors(num):

    out = set([1])
    for n in range(2,int(math.sqrt(num))+1):
        if num%n == 0:
            out.update([n, num//n])
    return out

def next(num):
    return sum(get_divisors(num))

def solve(limit):

    s = time.time()
    amicable_chains = {}
    invalid_chains = set()
    for n in range(1,limit+1):
        if n%limit//10==0: print(f'{n:_}')
        if n in invalid_chains or n in amicable_chains: continue
        num = n
        chain = [num]
        while True:
            # print(chain)
            num = next(num)
            if num == chain[0]:
                # is new amicable chain
                chain = set(chain)
                for i in chain:
                    amicable_chains[i] = chain
                break
            elif num in chain:
                # part of chain is amicable
                i = chain.index(num)
                amicable = set(chain[i:])
                invalid_chains.update(chain[0:i])
                for a in amicable:
                    amicable_chains[a] = amicable
                break
            elif (num in invalid_chains) or (num in amicable_chains) or num>limit:
                # whole chain is invalid because of limit, no amicable part found
                invalid_chains.update(chain)
                break
            chain.append(num)
    e = time.time()
    # print(list(amicable_chains.values()))
    longest = max(amicable_chains.values(),key = len)
    print(f"Longest amicable chain is {len(longest)}, with the smalles value of {min(longest)}. {e-s:f} seconds")

def seive_of_proper_div_sums(limit):
    array = [1]*(limit+1)
    for n in range(2,limit+1):
        for i in range(2,limit//n+1):
            array[i*n]+=n
    return array

def solveV2(limit):

    s = time.time()
    arr = seive_of_proper_div_sums(limit)
    longest = 0
    ans = 0
    seen = set()
    for n in range(1,limit+1):
        if n%(limit//10)==0: print(f'{n:_}')
        if n in seen: continue
        num = n
        chain = [num]
        while True:
            num = arr[num]
            if num == chain[0]:
                # is new amicable chain
                seen.update(chain)
                if len(chain)>longest:
                    ans = min(chain)
                    longest = len(chain)
                break
            elif num in chain:
                # part of chain is amicable
                i = chain.index(num)
                amicable = set(chain[i:])
                if len(amicable)>longest:
                    ans = min(amicable)
                    longest = len(amicable)
                seen.update(chain)
                break
            elif num in seen or num>limit:
                # whole chain is invalid because of limit, no amicable part found
                seen.update(chain)
                break
            chain.append(num)
    e = time.time()
    print(f"Longest amicable chain is {longest}, with the smalles value of {ans}. {e-s:f} seconds")

# solve(1_000_000)
solveV2(1_000_000_00)

# Longest amicable chain is 28, with the smalles value of 14316. 21.541808 seconds
# Longest amicable chain is 28, with the smalles value of 14316. 1.842450 seconds
