plaintext = 'one small step for man' # text to encrypt
ciphertext = '' # encrypted text
key = 14 # key number
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # letters of alphabet

plaintext = plaintext.upper().replace(' ', '') # this will make your message all caps and remove spaces

import re
plaintext = re.sub(r'[^\w\s]','',plaintext) # remove all punctuation from message

for letter in plaintext: # for loop
    newposition = LETTERS.find(letter) + key # find new position of letter
    newposition = newposition % 26 # ensure new position is between 0 and 25
    newletter = LETTERS[newposition] # find letter that corresponds to the new position
    ciphertext = ciphertext + newletter # add new letter to ciphertext
    
print(ciphertext) # display encrypted text
