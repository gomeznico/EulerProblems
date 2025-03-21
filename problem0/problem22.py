"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
3+15+12+9+14 = 53 is the 938th name in the list. So, COLIN would obtain a score of
53 * 938

What is the total of all the name scores in the file?
"""

import string
alphabet = string.ascii_uppercase
letter_score = {}
for i in range(26):
    letter_score[alphabet[i]] = i+1

f = open('names.txt','r')
names = sorted(f.read().split(','))

score = 0
for i,name in enumerate(names):
    name = name.replace('"','')
    name = name.replace('\n','')
    letters = 0
    for c in name:
        letters+= letter_score[c]
    # print(name, i+1, letters)
    name_score = (i+1)*letters
    score+=name_score
print(score)
# 871198282
