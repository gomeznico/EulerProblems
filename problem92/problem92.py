"""
Problem 92

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
For example,

44 (16+16) to 32 (9+4) to 13 to 10 to  1 to  1
85 to mathbf{89} to 145 to 42 to 20 to 4 to 16 to 37 to 58 to mathbf{89}

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
How many starting numbers below ten million will arrive at 89?
"""

## Brute Force: iterate thorugh to chain until 1 or 89 reached, keep count for each

## with DP, iterate through and keep memo of all numbers and where they end.
# for each step in chain, check if n in memo already
# add all prev numbers to memo, since they are all guaranteed to be new and end at same number

import time
def step(n):
    out = 0
    for c in str(n):
        out += int(c)*int(c)
    return out

print(step(44))

def solve(limit):
    s = time.time()
    nums_to_1 =set([1])
    nums_to_89 =set([89])

    for n in range(limit):
        chain = [n]
        num = n
        while num:
            num = step(num)
            if num in nums_to_1:
                nums_to_1.update(chain)
                break
            if num in nums_to_89:
                nums_to_89.update(chain)
                break
            chain.append(num)
        # if n%1_000_000 == 0: print(f'checking {n}')
    nums_under_limit = [n for n in nums_to_89 if n<limit]
    e = time.time()
    print(f"{len(nums_under_limit):_} numbers found under {limit:_}. {e-s:f} seconds ")


# solve(100_000)
# solve(1_000_000)
solve(10_000_000)
# solve(100_000_000)

# 85_623 numbers found under 100_000. 0.099964 seconds
# 856_929 numbers found under 1_000_000. 1.147910 seconds
# 8_581_146 numbers found under 10_000_000. 13.839607 seconds <--
# 85_744_333 numbers found under 100_000_000. 147.768796 seconds


# increasing input x10 -> runtime ~x11
# O(n) runtime.  each 'chain' is about same length until a prev number found
