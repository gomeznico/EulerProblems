"""
Problem 100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(text{BB}) = (15/21) * (14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 10^{12} = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.
"""
import math,time

# b = num blue
# r = num red

# b/(b+r) * (b-1)/(b+r-1) = 1/2
# 2b*(b-1) = (b+r)(b+r-1)
# 2b^2 - 2b = (T)(T-1)
# 2b^2 - 2b - [term] = 0
# use quad. eq

# b = 2 +/- sqrt(4 - 4*2*[-term]) / 2*2
# for b to be int, term under sqrt() must be int
# -1 - 8*term = perf. sq

def is_perfect_sq(num):
    n = int(math.sqrt(num)) - 3
    while n*n < num:
        n+=1
    if n*n == num:
        return n
    return False

def solve(start):
    # term = total*(total-1)
    # 2b^2 - b - [term] = 0
    # b = 1 +/- sqrt(-1 - 4*2*[term]) / 2*2

    s = time.time()
    found = False
    i = 0
    while not found:
        total = start+i
        if i % 1_000_000 == 0:
            print(f'checking at total: {(total):_}')
        term = total*(total-1)
        radical = 4 + 8*term
        n = is_perfect_sq(radical)
        if n:
            if (2+n)%4  == 0:
                blue = (2+n)//4
                break
            if (2-n)%4  == 0:
                blue = (2+n)//4
                break
        i+=1

    e = time.time()
    print(f"Number of blue discs found would be {blue}. {e-s} seconds elapsed")


solve(pow(10,12))


