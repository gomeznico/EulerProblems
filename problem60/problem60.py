"""
Problem 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""
import math
import itertools
from collections import defaultdict

def is_prime(n,primes):
    ## check if last prime is applicable
    ## add primes if req'd

    while primes[-1]<math.sqrt(n):
        add_next_prime(primes)

    ## check input number
    for factor in primes:
        if factor > math.sqrt(n): break
        if n%factor == 0: return False
    return True

def add_next_prime(primes):
    p = primes[-1]+2
    while not is_prime(p,primes):
        p+=2
    primes.append(p)

def is_valid_family(family:tuple ,primes:list, invalid_pairs:set):
    # check each conc. pair
    pairs = itertools.combinations(family,2)
    for a,b in pairs:
        if (a,b) in invalid_pairs: return False
        comb1 = int(str(a)+str(b))
        comb2 = int(str(b)+str(a))
        if not is_prime(comb1,primes) or not is_prime(comb2,primes):
            invalid_pairs.add((a,b))
            return False
    return True

def find_family(size,primes):
    notFound = True
    family = primes[0:size]
    upper_bound = size-1
    invalid_pairs = set()

    if is_valid_family(family,primes,invalid_pairs):
        notFound=False
        print(family)
    sub_family = tuple(family[0:-1])


    while notFound:
        if upper_bound%10 == 0:
            print(upper_bound, len(primes))
        # get next single prime
        upper_bound+=1
        while upper_bound >= len(primes):
            add_next_prime(primes)
        n = primes[upper_bound]

        ## get all comb. of size-1 from below bound, add
        for sub_family in itertools.combinations(primes[0:upper_bound], size-1):
            # check for invalid pairs in subfamily
            family = (sub_family) + (n,)
            if is_valid_family(family,primes,invalid_pairs):
                notFound = False


### better method 2:  find valid pairs, then build up the family
def is_valid_pair(a,b,primes):
    comb1 = int(str(a)+str(b))
    comb2 = int(str(b)+str(a))
    if not is_prime(comb1,primes) or not is_prime(comb2,primes):
        return False
    return True

def has_family_size(size,p,dictonary):
    # find some combination with intersection of len >=size

    # only check NEWLY made pairs, i.e. check all the families of those valid
    # with latest prime p, since only those valid with p could have had new pairs added in the latest step

    #
    families_of_p = []
    for s in dictonary[p]:
        families_of_p.append(dictonary[s])


    for family in itertools.combinations(families_of_p, size):
        common_elements = set.intersection(*family)
        if len(common_elements) >=size: return common_elements

    return False


# a = b = c = {1,2,3,4,5}
# d = {2,3,4,5,6}

# arr = [a,b,c,d]

# common = set.intersection(*arr)
# print(common)

# arr = ['a','b','c']
# common.update(arr)
# print(common)

# primes = [2,3]
# print(is_valid_pair(3,7,primes))


def find_family_v2(size):
    # valid_pairs = set()
    valid_with = defaultdict(set)         # dict key = int, -> set of valid concat pairs with int


    upper_bound = 0
    primes = [2,3]
    found = False
    while not found:
        if upper_bound%50 == 0:
            print(upper_bound, len(primes))
        # get next single prime
        upper_bound+=1
        while upper_bound >= len(primes):
            add_next_prime(primes)



        #generate new pairs with next possible prime
        p2 = primes[upper_bound]
        for p1 in primes[0:upper_bound]:
            if is_valid_pair(p1,p2,primes):
                pair = (p1,p2)
                # valid_pairs.add(pair)
                valid_with[p1].update(pair)
                valid_with[p2].update(pair)

        # check dict if family is possible from valid pairs
        family = has_family_size(size,p2,valid_with)
        if family:
            found = True
            print(family, f'checksum is {sum(family)}')
            print(upper_bound, len(primes))
            break

    # print(valid_with[3])
    # print(valid_with[7])
    # print(valid_with[109])


find_family_v2(4)
find_family_v2(5)
