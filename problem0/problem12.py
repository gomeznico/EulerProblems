
import math
def get_nth_traingle_num(n):
    arr = list(range(n+1))
    ans = sum(arr)
    return ans

def get_divisors(nth):
    num = get_nth_traingle_num(nth)
    div = set()
    i=1
    while i < math.sqrt(num):
        if num%i == 0:
            div.add(i)
            div.add(num/i)
        i+=1
    return len(div)

i = 1
while get_divisors(i) < 500:
    i+=1
print(get_nth_traingle_num(i))







