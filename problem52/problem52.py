"""
Problem 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def have_same_digits_arr(arr):
    # created set of sorted strings.  check length
    nums = [''.join(sorted(str(a))) for a in arr]
    nums = set(nums)
    return len(nums) == 1

def find_num_with_multiples(x):
    notfound = True
    num = 1
    while notfound:
        # lead digits must be 10->16. more than 16 will change len of num at 6x
        nums = [num*i for i in range(1,x+1)]
        if have_same_digits_arr(nums):
            print(nums)
            notfound = False
            break
        num +=1

# 2x -> 125874
# 6x -> 142857 correct!
