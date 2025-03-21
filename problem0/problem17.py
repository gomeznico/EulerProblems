"""
If the numbers 1to5
 are written out in words: one, two, three, four, five, then there are 3+3+5+4+4
 letters used in total.

If all the numbers from
 to
 (one thousand) inclusive were written out in words, how many letters would be used?
"""
# threehundredandfortytwo
map = {
    0:'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    # 100:'hundred',
    1000: 'onethousand'
}
def number_name(num):
    s = str(num)
    if num == 0:
        return None

    elif num in map: name = map[num]
    elif len(s) == 2:
        ones = num%10
        tens  = int(s[-2]+'0')
        name = map[tens] + map[ones]
    elif len(s) == 3:
        hundreds = int(s[0])
        name = map[hundreds]+'hundred'
        tens = number_name(int(s[1:]))
        if tens is not None:
            name = name + 'and'+tens
    return name

num_char = 0
for i in range(1,1001):
    num_char+= len(number_name(i))
print(num_char)






