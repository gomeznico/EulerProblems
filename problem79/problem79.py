"""
Problem 79

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
The text file, keylog.txt, contains fifty successful login attempts.
Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""
import itertools
import time
from collections import defaultdict

keylog = open('problem79/keylog.txt','r').read()[0:-1].split('\n')
# 50 attempts of 3 random digits.
keylog = [[int(n) for n in list(line)] for line in keylog]
# each attempt is arr of ints

# first check which digits compose the password, some may be excluded
## digits = 0,1,2,3,6,7,8,9 -> 8 total, 4 and 5 not included
digits = set()
for arr in keylog:
     digits.update(arr)
print(digits)

## Brute Force:
## generate passwords of increasing length, check if valid, go to next if not
## for first pass, minimum password must include at least 1 of each digit
## try all passwords of len=8 => 8! combinations => ~40,000 only

def is_valid_attempt(password,attempt):
    # pw: (1,2,3,4,5,6,7,8,9)
    # attempt : [3,1,7]

    ## iterate through password
    # when find any 1st number, start looking for 2nd num
    # when find any 2nd number, start looking for 3rd num
    i = 0
    for n in password:
        if n == attempt[i]:
            i+=1
            if i == len(attempt): return True
    return False

def is_valid_password(password:tuple, keylog):
    valid = True
    for attempt in keylog:
        if not is_valid_attempt(password,attempt):
            valid = False
            break
    return valid

def solve():
    i = 0
    s = time.time()
    for pw in itertools.permutations(digits,8):
        i+=1
        if i%10_000 == 0: print(i, pw)
        # if set(pw) != digits: continue
        if is_valid_password(pw,keylog):
            print('')
            break
    e = time.time()
    ans = ''.join([str(n) for n in pw])

    print(f'valid password found: {int(ans)} in {1000*(e-s):f} micro-seconds')

solve()

## Graph Solution
# create network where each node points fwd to what occurs afterwards
# then find path through the graph
## assume graph has a start and end point. i.e. a first digit with only fwd and a last digit with no fwd


class Network(object):
    ## assume unique soln exists, where each digit is used only once

    def __init__(self,keylog):
        self.keylog = keylog
        self.nodes = []
        self.fwd_neighbors = defaultdict(set)
        self.back_neighbors = defaultdict(set)

        self.build_network(keylog)


    def build_network(self,keylog):
        for attempt in keylog:
            a,b,c = attempt
            self.fwd_neighbors[a].update([b,c])
            self.fwd_neighbors[b].add(c)
            self.back_neighbors[c].update([a,b])
            self.back_neighbors[b].add(a)

        # convert to ordered list
        nodes = list(self.back_neighbors.keys()) + list(self.fwd_neighbors.keys())
        nodes = set(nodes)
        for key in nodes:
            self.fwd_neighbors[key] = sorted(self.fwd_neighbors[key])
            self.back_neighbors[key] = sorted(self.back_neighbors[key])
        self.nodes = nodes

    def get_start(self):
        # start will have 0 backward neighbors
        start = [n for n in self.back_neighbors if self.back_neighbors[n] == []]
        return start[0]

    def find_path(self):
        ##netwrok built
        ## find a valid path that visits every node
        s = time.time()
        start = self.get_start()

        ## assume each digit is used only once
        start_path = (start,)
        first_node = (start,start_path)
        stack = [first_node]

        seen  = set()

        while stack:
            curr = stack.pop()
            num,path = curr

            ## check if path is valid
            ## assume each digit is used only once
            if set(path) == self.nodes:
                pw = ''.join([str(n) for n in path])
                e = time.time()
                print(f'valid password found: {pw} in {1000*(e-s):f} micro-seconds')
                return

            seen.add(curr)

            for neighbor in self.fwd_neighbors[num]:
                node = (neighbor,path+(neighbor,))
                if node in seen: continue
                stack.append(node)

        print('path not found in network using all digits')


network = Network(keylog)
network.find_path()


