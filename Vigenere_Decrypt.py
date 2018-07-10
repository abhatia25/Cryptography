plaintext = ''
ciphertext = open('kasiski-handout-ciphertext.txt').read()

ciphertext = ciphertext.upper().replace(' ','')

password = 'JOKE'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigencode(cipherletter, keyletter):

    ciphernum = LETTERS.find(cipherletter)
    keynum = LETTERS.find(keyletter)

    plainnum = (ciphernum - keynum) % 26
    plainletter = LETTERS[plainnum]
    
    return plainletter

for i in range(0, len(ciphertext) ):
    plaintext += vigencode( ciphertext[i], password[i % len(password)] )

print(plaintext)
