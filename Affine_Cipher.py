plaintext = "''" # decrypted text
ciphertext = 'FBBCF BZCCW BJVJZ YAYZN BZCBD PWCTN YTNR' # encrypted text
additivekey = 11 # additive key number
multiplicativekey = 7 # multiplicative key number
multiplicativeinverse = 15 # multiplicative inverse of multiplicative key in modulo 26
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # letters of alphabet
mode = 'decrypt' # encrypt or decrypt

plaintext = plaintext.upper().replace(' ', '') # this will make your message all caps and remove spaces

import re
plaintext = re.sub(r'[^\w\s]','',plaintext) # remove all punctuation from message

ciphertext = ciphertext.upper().replace(' ', '') # all caps, no spaces

if mode == 'encrypt': # encryption mode
    t = 0 # initialize counter
    for i in plaintext: # for loop
        cipherposition = LETTERS.find(i) # find position of plaintext letter
        cipherposition = cipherposition + additivekey # apply additive key
        cipherposition = cipherposition * multiplicativekey # apply multiplicative key
        cipherposition = cipherposition % 26 # ensure it is between 0-25
        cipherletter = LETTERS[cipherposition] # find new letter
        ciphertext = ciphertext + cipherletter # add new letter to ciphertext
        t = t + 1 # increment counter
        if t % 5 == 0: # after every 5 characters
            ciphertext = ciphertext + ' ' # add space in ciphertext
    print(ciphertext) # display encrypted text

if mode == 'decrypt': # decryption mode
    while multiplicativeinverse < 26:
        if (multiplicativekey * multiplicativeinverse) % 26 == 1:
            for i in ciphertext: # for loop
                plaintextposition = LETTERS.find(i) * multiplicativeinverse - additivekey # compute new position
                plaintextposition = plaintextposition % 26 # ensure it is between 0-25
                plainletter = LETTERS[plaintextposition] # find plaintext letter
                plaintext = plaintext + plainletter # add plaintext letter to plaintext
            else:
                multiplicativeinverse += 1
        

    print(plaintext) # display decrypted text

