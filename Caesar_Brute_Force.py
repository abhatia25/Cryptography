ciphertext = 'RZGGYJIZTJPQZXMVXFZYVXVZNVMNCDAOBJJYAJMTJPDONIJOGDFZOCDNDNVXDKCZMOCVOKZJKGZCVQZWZZIPNDIBAJMJQZMORJOCJPNVIYTZVMNTJPKMJWVWGTRJMFZYAJMCJPMNOJNJGQZOCDNXCVGGZIBDIBKMJWGZHDATJPOCJPBCOOCDNRVNCVMYRVDOPIODGTJPNZZOCZJOCZMNWMPOZAJMXZHVTCVQZRJMFZYAJMOCZORZIOTNDSXJHWDIVODJINJIOCDNNDYZWPODORJIORJMFAJMOCZMZNOJAOCZWJSIJROCVOTJPCVQZXMVXFZYOCDNJIZTJPNCJPGYWVWGZOJMZAGZXOJICJRZVNTDORVNVIYXJINDYZMOCZZIDBHVOCVODNOCZMZNOJAOCDNWJSOVFZVYZZKWMZVOCVNTJPKGPIBZDIOJOCZYZKOCNJAOCZJOCZMXDKCZMOZSONJIOCDNWJSTJPRDGGWZXCVGGZIBZYBJJYGPXFKNOCZMZVMZVWNJGPOZGTIJNKZGGDIBZMMJMNDIOCDNKGVDIOZSORZKMJHDNZ'
plaintext = ''

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # letters of alphabet

ciphertext = ciphertext.upper()

cleanedtext = ''

for i in ciphertext:
    if i in LETTERS:
        cleanedtext += i

ciphertext = cleanedtext


for key in range(0,26):
    for i in ciphertext:
        newposition = LETTERS.find(i) + key # find new position of letter
        newposition = newposition % 26 # ensure new position is between 0 and 25
        newletter = LETTERS[newposition] # find letter that corresponds to the new position
        plaintext = plaintext + newletter # add new letter to ciphertext
    if 'THE' in plaintext:
        print('key: ' + str(key))
        print(plaintext)
    plaintext = ''
