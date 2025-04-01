"""
Problem 98

By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36^2. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.
Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
What is the largest square number formed by any member of such a pair?
NOTE: All anagrams formed must be contained in the given text file.
"""
import time, collections, itertools, math

words = open('problem98/words.txt','r').read()[0:-1].split(',')
words = [a[1:-1] for a in words]

## Brute Force
#go through each possible pair ~2000^2

## go through each word:
#   - determine 'mappings' that result in squares
#   - save mappings in dictionary of each word
## go through all pairs of words
#   - get intersection of each set of mappings


## smarter brute force through filte
def get_mappings(word,squares):
    letters = ''.join(sorted(set(word)))
    digits = '0123456789'

    out = set()
    ## generate possible mappings for word that result in square nums
    for ordering in itertools.permutations(digits,len(letters)):
        dig = ''.join(ordering)
        mapping = str.maketrans(letters,dig)
        number = word.translate(mapping)
        if int(number) in squares and number[0] != '0':
            out.add(frozenset(mapping.items()))
    return out

def solve(words):
    s = time.time()
    ## first sort by word lengths
    longest = len(max(words,key = len))
    words_by_len =[ [] for n in range(1,longest+2)]
    for word in words:
        words_by_len[len(word)].append(word)

    words_by_len = words_by_len[1:]

    ## looking for largest sq, so start with longest words -> largest numbers
    for group in words_by_len[::-1]:
        print(f'\nchecking {len(group)} words of length {len(group[0])}')

        ## find if any are anagrams of each other at all
        anagram_pairs = []
        for pair in itertools.combinations(group, 2):
            a,b = pair
            if sorted(a) == sorted(b): anagram_pairs.append(pair)

        print(f"{len(anagram_pairs)} anagrams pairs found")
        if len(anagram_pairs) == 0: continue  #go to next length of words

        ## create sq's of corect number of digits to check against
        longest = len(max(group,key = len))
        top = int(math.sqrt(int('9'*longest)))
        bot = int(math.sqrt(int('1'+'0'*(longest-1))))
        squares = set([n*n for n in range(bot,top+1)])

        ## only check/create mappings for pairs that are actually anangrams
        mappings = {}
        square_numbers = set()
        for pair in anagram_pairs:
            a,b = pair

            if a in mappings: a_maps = mappings[a]
            else:
                a_maps = get_mappings(a,squares)
                mappings[a] = a_maps
            if b in mappings: b_maps = mappings[b]
            else:
                b_maps = get_mappings(b,squares)
                mappings[b] = b_maps

            common_mappings = a_maps.intersection(b_maps)
            for m in common_mappings:
                mapping = dict(m)
                sq_pair = [int(a.translate(mapping)),int(b.translate(mapping))]
                square_numbers.update(sq_pair)


        print(f'{len(square_numbers)} valid square nums found')
        if len(square_numbers)>1:
            ans = max(square_numbers)
            break

    e = time.time()
    print(f"Largest square as a result of anagram-pair is {ans}. found in {e-s:f} seconds")

solve(words)
# largest square as a result of anagram-pair is 18769. found in 7.83495 seconds







