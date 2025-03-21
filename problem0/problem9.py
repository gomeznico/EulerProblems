"""
a pythagorean triple is a set wher a2 + b2 c2 dn a<b<c

for example, 3,4,5 are one

there exists exactly 1 triplet where a+b+c=1000
what is a*b*c
"""

def is_pyth_triple(a,b,c):
    if a>b or a>c or b>c:
        return False
    if (a*a + b*b) == (c*c):
        return True
    return False

def get_c(a,b):
    c = 1000 -a-b
    return c

def find_triple():
    triple =None
    for b in range(1,500):
        for a in range(1,b):
            c = 1000-a-b
            if is_pyth_triple(a,b,c):
                triple = (a,b,c)
                print(a*b*c)
                return triple
    print('not found')
print(find_triple())


