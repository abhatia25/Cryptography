ciphertext = ''
plaintext = ''
additivekey = 0
multiplicativekey = 0
multiplicativeinverse = 0

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # letters of alphabet

ciphertext = open('affine-challenge.txt').read()

ciphertext = ciphertext.upper()

cleanedtext = ''

for i in ciphertext:
    if i in LETTERS:
        cleanedtext += i

ciphertext = cleanedtext

multiplicativeinverses = {
    "1":1,
    "3":9,
    "5":21,
    "7":15,
    "9":3,
    "11":19,
    "15":7,
    "17":23,
    "19":11,
    "21":5,
    "23":17
    }


for additivekey in range(0,26):
    for key, val in multiplicativeinverses.items():
        for i in ciphertext:
            multiplicativekey = key
            print(ciphertext)
            multiplicativeinverse = val
            plaintextposition = LETTERS.find(i) * multiplicativeinverse - additivekey # compute new position
            plaintextposition = plaintextposition % 26 # ensure it is between 0-25
            plainletter = LETTERS[plaintextposition] # find plaintext letter
            plaintext = plaintext + plainletter # add plaintext letter to plaintext

##        if 'THE' in plaintext and 'AND' in plaintext:
##            print('additivekey: ' + str(additivekey))
##            print('multiplicativekey: ' + str(multiplicativekey))
##            print(plaintext)
##            plaintext = ''
            


