"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234 is 1 to 5 pandigital

the product 7254 is unusual since, 39x186=7254 contains 1->9 pandigital

find the sum of all products who's expression can be wrriten as pandigital 1->9

some products can be obtained in more than 1 way so be sure to only include it 1once in your answer
"""


##
## _ _ _  x _ _ _  = _ _ _ where each digit is only used once

## brute force go thorugh all a and b, where axb = c.  check if pandigital


def is_pandigital(a,b,c):
    eq = str(a)+str(b)+str(c)
    eq = ''.join(sorted(eq))
    if eq == '123456789': return True
    return False


products = set()
top_val = 10000
for a in range(1,top_val):
    for b in range(a+1,top_val):
        c = a*b
        if is_pandigital(a,b,c): products.add(c)
print(products)


# get all permutations, see if products are valid?
def get_all_perms(nums_str):
    ans =[]
    if len(nums_str)==1:
        ans.append(nums_str)
    else:
        perms = get_all_perms(nums_str[1:])
        n = nums_str[0]
        for perm in perms:
            for i in range(len(perm)+1):
                s = perm[0:i]+n+perm[i:]
                ans.append(s)
    return ans


## total perm => 9! = 362,880
## x ~ 100 choices for x and =
## total of 30 million checks

def is_pandigital(string):
    ## choose multipl. and eq sign location
    products = set()
    for i in range(1,10):
        for j in range(i+1,10):
            # for i=2, j=3
            # eq -> 12 x 3 = c

            a = int(string[0:i])
            b = int(string[i:j])
            c = a*b
            if str(c) == string[j:]: products.add(c)
    return products

# all_perms = get_all_perms('123456789')

# all_products = set()
# for p in all_perms:
#     new = is_pandigital(p)
#     all_products.update(new)
# print(all_products)
# print(sum(all_products))



