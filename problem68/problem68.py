"""
Problem 68

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.


Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

TotalSolution Set
9   4,2,3; 5,3,1; 6,1,2
9   4,3,2; 6,2,1; 5,1,3

10  2,3,5; 4,5,1; 6,1,3
10  2,5,3; 6,3,1; 4,1,5

11  1,4,6; 3,6,2; 5,2,4
11  1,6,4; 5,4,2; 3,2,6

12  1,5,6; 2,6,4; 3,4,5
12  1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
"""
import itertools
from collections import defaultdict
import time

def is_valid_family(family:list[tuple]):
    # soln = [a , b, c...]

    ## is valid if all sum to same val
    checksum = sum(family[0])
    for s in family:
        if sum(s) != checksum: return False

    ##check all are diff:
    checksum = set()
    for s in family:
        t = tuple(sorted(s))
        checksum.add(t)
    if len(checksum) != len(family): return False


    ## check ordering of the sets
    # all first el are diff
    checksum = set([s[0] for s in family])
    if len(checksum) != len(family): return False


    ## family must start with smallest 1st number
    first_num = family[0][0]
    checksum = min([s[0] for s in family])
    if checksum != first_num: return False


    # check 'cycle' of 2nd and 3rd els
    # pairs = [(a,b), (b,c), ...]
    pairs = list(zip(family, family[1:]+family[:1]))
    for a,b in pairs:
        x1,y1,z1 = a
        x2,y2,z2 = b
        if z1 != y2: return False
    return True


## get all possible combos - Brute Force
## V1 - worked for 3-gon
def create_set_families_V1(arr,n):
    all_perms_of_3 = list(itertools.permutations(arr,3))
    # for 3-gon -> 120 possible ordered combos of len 3     6*5*4
    # for 5-gon -> 720 possible ordered combos of len 3     10*9*8


    # for 3-gon, creates 120*119*118 = 1,685,040 poss familes to check
    # for 5-gon, creates 720*719*718*717*716 = 1.9e14 !! poss familes to check
    # all_familes = list(itertools.permutations(all_perms_of_3,n))

    # create_dict categorized by sums
    # for 3-gon, reduces num of families to check to 22,704 (74x reduction!!)
    perms_by_sum =defaultdict(list)
    for s in all_perms_of_3:
        num = sum(s)
        perms_by_sum[num].append(s)
        # in 3-gon, for sums 9,10,11,12: arr length = 18 -> 18*17*16 => 4_896 families in 1 sum to check
        # in 5-gon: for sums 15,16,17,18: arr length = 60 -> 60*59*58*57*56 = 655_381_440 families in 1 sum to check


    for s in perms_by_sum:
        print(f' sets that sum to {s} : {len(perms_by_sum[s])}')

    valid_families =[]
    for s in perms_by_sum:
        i = 0
        for fam in itertools.permutations(perms_by_sum[s],n):
            if i%5_000_000 == 0: print(f'checking sum = {s} and at step: {i:_}')
            if is_valid_family(fam): valid_families.append(fam)
            i+=1
        # family = (perm1,perm2, ...perm_n)
    return valid_families

def create_set_families_V2(arr,n):
    all_nums_set = set(arr)
    all_sets = list(itertools.combinations(arr,3))
    # for 3-gon -> 20 possible unordered sets for a group of 3
    # for 5-gon -> 120 possible unordered sets for a group of 3

    ## group into sets that sum to same num:
    sets_by_sum =defaultdict(list)
    for s in all_sets:
        num = sum(s)
        sets_by_sum[num].append(set(s))
        # in 3-gon, for sums 9,10,11,12: arr length = 3, only possible sets that can create a family of length 3 to chec
        # in 5-gon: for sums 15,16,17,18: arr length = 10 -> create families choosing 5 unique sets from each sum, then reoder as req'd

    # create ordered families with each sum
    valid_families =[]
    for s in sets_by_sum:
        # print(f' sets that sum to {s} : {len(sets_by_sum[s])} ' , sets_by_sum[s])
        valid_families += create_valid_families_from_sets(sets_by_sum[s], all_nums_set, n)


    return valid_families

def create_valid_families_from_sets(sets:list,all_nums_set:set,n:int):
    # assume sets already add up to same number
    # create all possible unordered combos with the sets
    ## ex: 3-gon
    ## sets that sum to 10: [{1,3,6}, {1,4,5}, {2,3,5}] -> only 1 combo of 3
    ## ex: 5-gon
    ## sets that add to 12: [{1,2,9}, {8,1,3}, {1,4,7}, {1,5,6}, {2,3,7}, {2,4,6}, {3,4,5}] -> 5*4*3 => 60 possible combos


    # get all possible unordered combos of choosing n sets:
    all_combos = list(itertools.combinations(sets,n))

    #filter all combos
    valid_combos =[]
    for combo in all_combos:
        ## check that total union includes all numbers from 1-10
        total_union = set().union(*combo)
        if total_union != all_nums_set: continue

        ## check that each set has 1 unique val.  this is the 'outer' number that can't be repeated in any other set
        unique_vals= set()
        for s in combo:
            remaining = [_ for _ in combo if _ !=s]
            unique = s - set().union(*remaining)
            if len(unique)==1:  unique_vals.update(unique)
        if len(unique_vals) != len(combo): continue

        ## combo = [{a,b,c}, {d,e,f}, {g,h,i}...]
        ## re-parse combo to be of form: -> [ (a,(b,c)), (d,(e,f)).... (unique_val, (val1,val2)) ]
        ## will reduce combinations further on from 6^n to 2^n
        parsed_combo =[]
        for s in combo:
            others = [_ for _ in combo if _ !=s]
            unique = s - set().union(*others)
            unique = unique.pop()
            s.discard(unique)
            a = (unique, tuple(s))
            parsed_combo.append(a)
        valid_combos.append(parsed_combo)


    # unordered combos of unordered sets
    valid_families =[]
    for combo in valid_combos:
        # combo = [ (a,(b,c)), (d,(e,f)).... (unique_val, (val1,val2)) ]

        for family_perm in itertools.permutations(combo,len(combo)):
            ## create arrays to use iter.product on
            arrays = []
            for line in family_perm:
                a = line[0]
                b,c = line[1]
                line_perms = [(a,b,c) ,(a,c,b)]
                arrays.append(line_perms)

            # each entry in ordered_families produced by iter.product is now guaranteed to be:
            #   1: have each line sum to the same value.
            #   2: each line is different from all others, no repeats of any sets of 3 vals
            #   3: the first vals of each line are all diff. from each other, and do not appear in 'inner ring'

            for ordered_family in itertools.product(*arrays):
                if is_valid_family(ordered_family): valid_families.append(ordered_family)





    # print(f' number for valid combos: {len(valid_combos)} \n')
    return valid_families

def concat(family):
    s = ''
    for a,b,c in family:
        s+=str(a)+str(b)+str(c)
    return int(s)

def display(family):
    checksum = sum(family[0])
    s =f'{checksum} => '
    for a,b,c in family:
        s+= f' {a},{b},{c};'
    print(s)


def solve_3gon():
    arr = [1,2,3,4,5,6]
    n = 3
    start = time.time()
    all_families = create_set_families_V1(arr,n)
    end = time.time()
    for l in all_families:
        display(l)
    checksum = max([concat(l) for l in all_families])
    print(checksum)
    print(f' it took {end-start:.5f} seconds to calculate soln for {n}-gon using algo_V1')
    # 0.02569 seconds
    # answer = 432621513

    start = time.time()
    all_families = create_set_families_V2(arr,n)
    end = time.time()
    for l in all_families:
        display(l)
    checksum = max([concat(l) for l in all_families])
    print(checksum)
    print(f' it took {end-start:.5f} seconds to calculate soln for {n}-gon using algo_V2')
    # 0.00036 seconds
    # answer = 432621513

def solve_5gon():
    print(f'Trying 5-gon now....')
    arr = [1,2,3,4,5,6,7,8,9,10]
    n= 5

    ## do V2 first, since much faster...
    start = time.time()
    all_families = create_set_families_V2(arr,5)
    end = time.time()
    for l in all_families:
        display(l)
    concats = [concat(l) for l in all_families if len(str(concat(l)))==16]
    print(max(concats))
    print(f' it took {end-start:.5f} seconds to calculate soln for {n}-gon using algo_V2')


    ## V1 brute force takes very long time...
    arr = [1,2,3,4,5,6,7,8,9,10]
    n= 5
    start = time.time()
    all_families = create_set_families_V1(arr,n)
    end = time.time()
    for l in all_families:
        display(l)
    concats = [concat(l) for l in all_families if len(str(concat(l)))==16]
    print(max(concats))
    print(f' it took {end-start} seconds to calculate soln for {n}-gon using algo_V1')


solve_3gon()
# V1 algo:
    # 0.02569 seconds
    # answer = 432621513
# V2 algo:
    # 0.00036 seconds       ~100x faster
    # answer = 432621513
solve_5gon()
# V2 algo:
    # 0.03110 seconds
    # answer = 6531031914842725
# V1 algo:
    # 6728.6762 seconds   ~1:52 hours
    # answer = 6531031914842725
