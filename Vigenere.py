plaintext = 'PIZZA IS TASTY'
ciphertext = ''

plaintext = plaintext.upper().replace(' ','')

password = 'DOG'

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigencode(plainletter, keyletter):

    plainnum = LETTERS.find(plainletter)
    keynum = LETTERS.find(keyletter)

    ciphernum = (plainnum + keynum) % 26
    cipherletter = LETTERS[ciphernum]

    return cipherletter

for i in range(0, len(plaintext) ):
    ciphertext += vigencode( plaintext[i], password[i % len(password)] )

print(ciphertext)
    
