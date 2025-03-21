"""
a unit fraction is a fraction with 1 in the numerator

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10= 0.1

the (x) indicates a repeating cycle of digits
for what value of d where d<1000 will 1/d have the longest recurring cycle?
"""

def long_div_sim(denom):
    # 1 / denom => 10 - (multiple of denom) = remainder
    #                   multiple is the 'digit' in decimal
    #               remainder*10 - (multiple of denom) = new_remaineder -> repeat
    # repeat is found when a remainder shows up again
    # decimal does not repeat when remainder == 0
    # 

    numerator = 10
    digits = []
    remainders = []
    curr = numerator
    repeats = True
    while True:
        digit = curr//denom
        curr = curr%denom
        digits.append(digit)
        if curr in remainders: break

        remainders.append(curr)
        curr = curr*10

        if curr == 0:
            repeats = False
            break

        while curr < denom:
            curr*=10
            digits.append(0)
    # remove leading non-repeating 'digits'
    if repeats:
        while remainders[0] != curr: remainders.pop(0)
    length = len(remainders)
    sequence = digits[-length:]
    # print(denom, sequence, repeats)
    return(sequence,repeats)


maximum = (1,0)
for i in range(2,1000):
    sequence , repeats = long_div_sim(i)
    if repeats and len(sequence)>maximum[1]:
        maximum = (i,len(sequence))

print(maximum)
print(long_div_sim(maximum[0]))






