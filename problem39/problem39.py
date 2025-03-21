"""
Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?

"""
from collections import defaultdict

# p = a+b+c

# p = a + b + sqrt(a2 + b2)

# P = 3->1000


# a -> [1,333]
# b -> [1,333]
# c = sqrt(a2 + b2)

# c-> [1,333]

# a+b+c = 1000 at max


valid_p =[[0,'']]*1001


valid_p =defaultdict(list)

for a in range(1,400):
    for b in range(a,400):
        for c in range(b+1,500):

            if a*a + b*b == c*c:
                p = a+b+c
                if p<=1000:
                    valid_p[p].append((a,b,c))

a = max(valid_p, key=lambda x:len(valid_p[x]))
print(a, valid_p[a])
