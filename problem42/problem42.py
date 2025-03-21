"""
Problem 42

The nth term of the sequence of triangle numbers is given by, t_n = 1/2 * n(n+1); so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t_{10}. If the word value is a triangle number then we shall call the word a triangle word.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
s = open("problem42/0042_words.txt",'r').read()
s = s.split(',')

def word_val(word):
    val = 0
    for s in word:
        if s.isalpha():
            val+= ord(s)-64
    return val

def is_triangle(num):
    if num == 1: return True

    i =1
    triangle = 1
    while num > triangle:
        i+=1
        triangle = i*(i+1)//2
        if num == triangle: return True
    return False

num_triangle_words = 0

for word in s:
    val = word_val(word)
    if is_triangle(val): num_triangle_words+=1

print(num_triangle_words)
# 162
