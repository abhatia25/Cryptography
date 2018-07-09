plaintext = 'Zebras Eat Grass!'
ciphertext = ''
key = 3                                    # key can be between 0 and 95
mode = 'encode'                            # set to encode or decode

def encipherchar(char, mykey):
  position = ord(char)                     # Gets ASCII number between 32 - 126 for the character (95 visible characters) 
  newposition = position - 32 + mykey      # Subtracts 32 so position is between 0 and 94, then adds key
  newerposition = newposition % 95         # mod 95 so all positions between 0 and 94 again
  finalposition = newerposition + 32       # Add 32 so now all positions between 32 and 126 again

  cipherletter = chr(finalposition)        # convert final ASCII number to ASCII character

  return cipherletter

def decipherchar(char, mykey):
  position = ord(char)                     # Gets ASCII number between 32 - 126 for the character 
  newposition = position - 32 - mykey      # Subtracts 32 so position is between 0 and 94, then subtracts key
  newerposition = newposition % 95         # mod 95 so all positions between 0 and 94 again
  finalposition = newerposition + 32       # Add 32 so now all positions between 32 and 126 again

  plainletter = chr(finalposition)         # convert final ASCII number to ASCII character

  return plainletter
 
 
if mode == 'encode':
  for i in plaintext:                      # Takes each character in the string, plaintext, calls it i
    ciphertext += encipherchar(i,key)      # sends the character, i, to encipherchar function with key

  print(ciphertext)

if mode == 'decode':
  for i in ciphertext:                     # Takes each character in the string, ciphertext, calls it i
    plaintext += decipherchar(i,key)       # sends the character, i, to decipherchar function with key
 
  print(plaintext) 
