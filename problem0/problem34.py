"""
145 is a curious number, the sum of its digit factorials is itesld
1! + 4! + 5! = 1+24+120 = 145

find the sum of all numbers that are this way

1 and 2 dont count

"""
import math
#9! = 362000
# 9!+9!+9!+9!+9!+9! = ~2.2 million,  six 9's
#9,9,9,9,9,9,9 => 2.6 million -> max value to consider is 2.6 million

# max of 7 digits

def is_curious(num):
    string = str(num)
    sum = 0
    for c in string:
        sum += math.factorial(int(c))
    if sum == num: return True
    return False

curious =set()
for n in range(3,2999999):
    if is_curious(n): curious.add(n)

print(len(curious))
print(curious)
print(sum(curious))
