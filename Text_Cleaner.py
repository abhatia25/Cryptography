plaintext = 'For all who are reading this, hello. You have solved this complex enigma cipher. We have used a series of techniques that the average person would not be capable of doing without the assistance of our wonderful teacher, Mr. Gibson, and our TA, Thomas. We have spent the week of July Eighth learning all about ciphers such as the Vigenere, Hill, Caesar, and Enigma. Despite all the use of cryptography in the past, it remains a fascinating science that proves to be fundamental for the future. '
cleanedtext = ''

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

plaintext = plaintext.upper()

for i in plaintext:
    if i in LETTERS:
        cleanedtext += i

plaintext = cleanedtext



print(cleanedtext)
