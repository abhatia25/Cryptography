message = 'hello, this is my test message' # message to be translated
message = message.upper()                  # redefines the message in uppercase letters
translated = ''                            # creates empty string that I will store reversed message
index = len(message) - 1                   # figure out how long the message is, then subtract 1
                                           # to compute the index of the last character

while index >= 0:                          # while the index is greater than or equal to 0
 if message[index] != ' ':                 # if the current letter isn't a space, then...
   translated += message[index]            # a different way to append the character from 
                                           # message to the end
 index = index - 1                         # subtract 1 from index to move to the next character

print(translated)                          # when the index is not >= 0, print the string translated

if i == 3:
  print('i equals 3!')

if i != 3:
  print('Hey everyone! i doesn't equal 3!')

if 'e' in 'test':
  print('Yeah, there's a letter e in the word test')

if 'e' not in 'math':
  print('Nope. No letter e's in the word math')
 
  
