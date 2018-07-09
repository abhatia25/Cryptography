plaintext = ''
ciphertext = ''
password = 'DOG'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # letters of alphabet

plaintext = open('Longish_Passage.rtf').read()

plaintext = plaintext.upper()

cleanedtext = ''

t = 0

for i in plaintext:
    if i in LETTERS:
        cleanedtext += i

plaintext = cleanedtext

def vigencode(plainletter, keyletter):
    
    plainnum = LETTERS.find(plainletter)
    keynum = LETTERS.find(keyletter)

    ciphernum = (plainnum + keynum) % 26
    cipherletter = LETTERS[ciphernum]

    return cipherletter

for i in range(0, len(plaintext) ):
    ciphertext += vigencode(plaintext[i], password[i % len(password)])
    t += 1
    if t % 5 == 0: # after every 5 characters
        ciphertext = ciphertext + ' ' # add space in ciphertext

print(ciphertext)
    

