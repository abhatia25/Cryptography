ciphertext = '' # only needed if mode is decrypt
plaintext = '' # only needed if mode is encrypt
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

mode = 'decrypt' # encrypt or decrypt

key = '' # only needed if mode is encrypt

from Tools import *

ciphertext = open('challenge03b.txt').read() 

if mode == 'decrypt':
    ciphertext = ciphertext.upper().replace(' ','')
    cleanedtext = ''

    for i in ciphertext:
        if i in LETTERS:
            cleanedtext += i
    ciphertext = cleanedtext

    keylength = 0
    currentkey = 0
    pile1 = [''] * keylength

    keylength = KeyApproximator(ciphertext)

    for pile in splitter(ciphertext, keylength):
        pile1[count] = pile
        count += 1

    
if mode == 'encrypt':
    plaintext = plaintext.upper().replace(' ','')
    cleanedtext = ''

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
        ciphertext += vigencode( plaintext[i], key[i % len(key)] )

    print(ciphertext)
    




