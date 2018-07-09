message = 'hello, this is my test message' # defines the message to be translated
translated = ''                            # creates empty string that will store reversed message
index = len(message) - 1                   # figures out how long the message is, then subtracts 1
                                           # to compute the index # of the last character
                                           # for this example, index would equal 29 since there are
                                           # 30 characters in the example message

while index >= 0:                          # while the index is greater than or equal to 0
 translated = translated + message[index]  # append the character from message to the end
 index = index - 1                         # subtract 1 from index to move to the previous character

print(translated)                          # once the loop finishes, print the string translated
