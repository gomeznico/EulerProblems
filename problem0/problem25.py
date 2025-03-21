"""
Fibonacci sequence
1 1 2 3 5 8 13 21 34 55 89 144
the twelth term is 144, whihc has 3 digits

what is the index of the first term to contain 1000 digits
"""

def fibonacci_memo(index, memo={1:1,2:1}):
    if index in memo: return memo[index]

    f_a = fibonacci_memo(index-1, memo)
    f_b = fibonacci_memo(index-2, memo)
    memo[index] = f_a+f_b
    return f_a+f_b

def fibonacci_recursion(index):
    # if index in memo: return memo[index]
    if index <3: return 1
    f_an = fibonacci_recursion(index-1)
    f_bn = fibonacci_recursion(index-2)
    return f_an+f_bn

index = 10
while len(num) < 1000:
    index+=1
    num = str(fibonacci_memo(index))

print(num)
print(len(num))
print(index)
