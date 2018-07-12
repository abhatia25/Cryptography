plaintext = ''
ciphertext = ''
keyword = 'DOG'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key=[] * 25

accumulator = 0
for i in keyword:
    key[accumulator] = i
