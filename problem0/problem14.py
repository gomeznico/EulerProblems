"""
longest collatz seq
for n is even -> n/2
for n is odd -> 3n+1

starting with n=13, sequence is

13 , 40, 20, 10, 5, 16, 8, 4, 2, 1
contains 10 terms

what # under 1million has the longest chain
"""

def get_next(num):
    if num%2 == 0: return num/2
    else: return 3*num +1

chain_lengths = {}
max_start = (1,1)
for i in range(1,1000000):
    num = i
    count = 1
    while num != 1:
        num = get_next(num)
        if num in chain_lengths:
            count += chain_lengths[num]
            break
        count +=1
    chain_lengths[i] = count
    if count > max_start[1]:
        max_start = (i,count)
# print(chain_lengths)
print(max_start)




# {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17, 8: 4, 9: 20, 10: 7, 11: 15, 12: 10, 13: 10, 14: 18, 15: 18, 16: 5, 17: 13, 18: 21, 19: 21}
# {1: 1, 2: 2, 3: 8, 4: 3, 5: 6, 6: 9, 7: 17, 8: 4, 9: 20, 10: 7, 11: 15, 12: 10, 13: 10, 14: 18, 15: 18, 16: 5, 17: 13, 18: 21, 19: 21}

