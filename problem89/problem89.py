"""
Problem 89

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.
For example, it would appear that there are at least six ways of writing the number sixteen:
IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI
However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.
The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.
Find the number of characters saved by writing each of these in their minimal form.
Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""



test = """IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI"""

### Method 1: read then recreate
# all nums are guaranteed valid.  read to get actual value.  then use val to construct actual minimal roman num
# no more than 4 id. consecutive units. i.e. max possible val is ~4999 from 4000=MMMM and 900=DCCCC and 99=LXXXXIX

def parse(input:str):
    return input.split('\n')

def read_valid(line):
    val_of = {
    'I':1,
    'V':5,
    'X':10,
    'L':50,
    'C':100,
    'D':500,
    'M':1000,
    }
    num = 0
    prev_val = 1000
    for c in line:
        val = val_of[c]
        num += val
        if val > prev_val:
            # part of subtract. pair
            # subtract already counted prev_val
            # and the current subtract as well
            num += -2*prev_val
        prev_val = val
    return num

def romanize(num):
    ## create most valid roman numeral of number
    ## use largest nums first
    ## 'streaks' of 4 are valid
    s = ''
    # always add largest 'digit' possible
    digits = [
        (1,'I'),
        (5,'V'),
        (10,'X'),
        (50,'L'),
        (100,'C'),
        (500,'D'),
        (1000,'M'),
        (4,'IV'),
        (9,'IX'),
        (40,'XL'),
        (90,'XC'),
        (400,'CD'),
        (900,'CM'),
        # (4000,'MMMM'),
        ]
    # sorted by largest first
    digits = sorted(digits, reverse=True)
    while num !=0:
        for val,digit in digits:
            # add largest digt less than num
            if val<=num:
                s += digit
                num += -val
                break
    return s

def solve():
    input = open('problem89/roman.txt', 'r').read()[0:-1]
    roman_numerals = parse(input)

    total_characters_saved = 0
    for line in roman_numerals:
        shortend = romanize(read_valid(line))
        total_characters_saved += len(line)-len(shortend)
    print(total_characters_saved)

solve()
# 743

"""
rules:
1. descending size:  largest num/digits must be placed in order : XIX not IXX : (10+9) not (9+10)
2. M C X cannot be euqalled or succeeded by smaller denominations
3. D,L, V can only be used once in a string. XVIV invalid: (10+5+4), 19 is XIX

Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
I can only be placed before V and X.
X can only be placed before L and C.
C can only be placed before D and M.
# the rule of streaks of three was a guideline, not a rule...

49 can be written in multiple valid ways
XXXX IIIIIIIII
XXXX VIIII
XXXX IX
XL IIIIIIIII
XL VIIII
XL IX most compact
"""
