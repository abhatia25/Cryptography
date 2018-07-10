plaintext = ''
ciphertext = ''
password = 'PIZZA'
key = 17
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # letters of alphabet

ciphertext = open('caesar_challenge_1.txt').read()

ciphertext = ciphertext.upper()

cleanedtext = ''

t = 0

for i in ciphertext:
    if i in LETTERS:
        cleanedtext += i

ciphertext = cleanedtext

for letter in ciphertext:
    position = LETTERS.find(i)        
    newposition = position - key      # Subtracts the key to the position to determine the new position
    finalposition = newposition % 26  # Determine the final position by taking newposition mod 26
    plaintext += LETTERS[finalposition] # Adds whatever letters is in the finalposition to plaintext
 
def vigencode(plainletter, keyletter):
    
    plainnum = LETTERS.find(plainletter)
    keynum = LETTERS.find(keyletter)

    ciphernum = (plainnum + keynum) % 26
    cipherletter = LETTERS[ciphernum]

    return cipherletter

for i in range(0, len(plaintext) ):
    ciphertext += vigencode(plaintext[i], password[i % len(password)])
    t += 1
    if t % 5 == 0:
        ciphertext = ciphertext + ' '

from Tools import *

barchart(ciphertext, 'monday_graph.svg')


