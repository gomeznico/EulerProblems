"""
the fraction 49/98 is curious.  if you incoreectly cancel out the nines, you get 4/8, whihc happens to be correct.

fractions like 30/50 = 3/5 is trivial

there are exactly 4 non trivial examples of these fractions
 where it is less than 1
 where a and b both have 2 digits (a/b)
 if you multiply the 4 fractions together, what is the value of the denominator when it is simplified?

"""


def fraction_reduced(a,b):
    # a < b
    true_val = a/b
    a_s = str(a)
    b_s = str(b)
    if a_s[0] in b_s:
        b_s = b_s.replace(a_s[0],'',1)
        a_s = a_s[1]
    elif a_s[1] in b_s and a_s[1] !='0':
        b_s = b_s.replace(a_s[1],'',1)
        a_s = a_s[0]


    if (int(a_s) == a and int(b_s)==b)or b_s == '0':
        # print('vals not reduced')
        return False
    wrong = int(a_s)/int(b_s)
    # print(a,b,true_val, wrong)
    if wrong == true_val:
        return (a,b)

valid = set()
for a in range(10,99):
    for b in range(a+1,100):
        if fraction_reduced(a,b):
            valid.add((a,b))

num,denom =1,1
for a,b in valid:
    num *= a
    denom*= b
print(num/denom)







