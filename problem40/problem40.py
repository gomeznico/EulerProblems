"""
Problem 40

An irrational decimal fraction is created by concatenating the positive integers:
0 . 12345678910_1_112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
If d_n represents the nth digit of the fractional part, find the value of the following expression.
d_1 * d_{10} * d_{100} * d_{1000} * d_{10_000} * d_{100_000} * d_{1_000_000}
"""


#  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21...

# calculate length of dec. after x numbers concatinated
# 9 nums -> 1 digit long
# 90 nums-> 2 digits long
# 900 nums->3 digits long
# 9000      4 digits...
# 90_000    5 digits...
# 900_000   6 digits...
# 9_000_000 7 digits...

def get_nth_digit(n):
    # O(n) time - while loo is approx. n loops.
    # O(1) space - 2 arrays and the counter saved.  arrays grow very slowly

    if n<=9: return n
    i = 10
    digits = str(i)
    index = [10,11]
    while n not in index:       ## O(n)...very very slightly log? at large enough numbers
        i+=1
        digits = str(i)
        num_digits = len(digits)
        if digits == '1' + '0'*(num_digits-1):
            index =  [a+num_digits-1 for a in index] + [index[-1]+num_digits]
        else:
            index =  [a+num_digits for a in index]

    print(digits)
    print(index)

    j = index.index(n)
    return int(digits[j])

places = [1,10,100,1000,10_000,100_000,1_000_000]
ans = 1
for p in places:
    ans*= get_nth_digit(p)
print(ans)

get_nth_digit(1_000_000)
get_nth_digit(10_000_000)
get_nth_digit(100_000_000)
get_nth_digit(1_000_000_000)
