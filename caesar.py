plaintext = open('plaintext.txt').read()
ciphertext = ''
key = 17
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
mode = 'encode'

plaintext = plaintext.upper()                    # this will make your message all caps
ciphertext = ciphertext.upper().replace(' ', '') # this will make your message all caps and remove spaces

if mode == 'encode':
  ciphertext = ''
  for i in plaintext:                    # Takes each character in the string, plaintext, calls it i
    if i in LETTERS:
      position = LETTERS.find(i)         # Looks up i in the string LETTERS and returns the position
      newposition = position + key       # Adds the key to the position to determine the new position
      finalposition = newposition % 26   # Determine the final position by taking newposition mod 26

      ciphertext += LETTERS[finalposition] # Adds whatever letters is in the finalposition to ciphertext
      
      if len(ciphertext.replace(' ','')) % 5 == 0:
        ciphertext += ' '  

  print(ciphertext)

if mode == 'decode':
  plaintext = ''
  for i in ciphertext:                # Takes each character in the string, ciphertext, calls it i
    position = LETTERS.find(i)        # Looks up i in the string LETTERS and returns the position
    newposition = position - key      # Subtracts the key to the position to determine the new position
    finalposition = newposition % 26  # Determine the final position by taking newposition mod 26

    plaintext += LETTERS[finalposition] # Adds whatever letters is in the finalposition to plaintext
 
  print(plaintext.lower())            #retuns plaintext lowercase and without spacing
