"""
Problem 59

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
Your task has been made easy, as the encryption key consists of three lower case characters. Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
"""
import string

data = open('problem59/0059_cipher.txt','r').read()
data = data[0:-1]

# other='[](){}<>=+?!/\.,:; 1234567890'
# allowable_chars = string.ascii_lowercase + string.ascii_uppercase + other +'"'
# allowable_chars = set(list(allowable_chars))

not_allowed = '|~`#$%&'

alphabet = string.ascii_lowercase
# method 1
def decrypt(message,key):
    key = [ord(c) for c in key]
    message = message.split(',')
    message_out = []

    valid = True
    for i,char in enumerate(message):
        c = chr(int(char)^key[i%3])

        message_out.append(c)
        if c in not_allowed:
            print(c)
            # print(''.join(message_out))
        #     valid = False
            break
    return ''.join(message_out)

d = {}
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            key = a+b+c
            message = decrypt(data,key)
            if message: d[key] = message

max_key = max(d, key= lambda x:len(d[x]))
print(max_key, d[max_key])

s = [ord(c) for c in d[max_key]]
print(sum(s))

# method 2 - find message with most number of 'the'
def decrypt(message,key):
    key = [ord(c) for c in key]
    message = message.split(',')
    message_out = []

    for i,char in enumerate(message):
        c = chr(int(char)^key[i%3])
        message_out.append(c)

    return ''.join(message_out)

def score(message):
    out = 0
    for word in message.split():
        if word == 'the' or word == 'The':
            out+=1
    return out

def checksum(message):
    s = [ord(c) for c in message]
    return sum(s)


d = {}
best_key = [0,'']

for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            key = a+b+c
            message = decrypt(data,key)
            if score(message) > best_key[0]:
                d[key] = message
                best_key = [score(message),key]

print(best_key)
print(checksum(d[best_key[1]]))



