plaintext = 'arosebyanyothernamewouldsmellassweet'
rail1 = ''
rail2 = ''

plaintext = plaintext.replace(" ", "")

maxindex = len(plaintext) - 1
index = 0



while index <= maxindex:
  if index % 2 == 0:
    rail1 = rail1 + plaintext[index]
  else:
    rail2 = rail2 + plaintext[index]
  index = index + 1
  

ciphertext = rail1.upper() + rail2.upper()
print(ciphertext)
