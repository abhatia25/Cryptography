import random
def powerMod(base,exponent,modulus):
    order = bin(exponent)[2:]
    powerlist = [base]*(len(order))
    result = 1
    for i in range(1,len(powerlist)):
        powerlist[i] = (powerlist[i-1]**2) % modulus

    for i in range(len(order)):
        if order[i] == '1':
            result *= powerlist[len(order)-i-1]
            result = result % modulus
    return result

def textToBinary(text):
    return bin(int.from_bytes(text.encode(), 'big'))
def binToDec(n):
    return int(n, 2)
def decToBin(n):
    return int(bin(n), 2)
def binaryToText(n):
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def prime(p):
    if powerMod(2, p-1, p) == 1:
        return True
    return False
def randomPrime(digits):
    number = ''
    for i in range(digits):
        number += str(random.randint(0,9))
    number = int(number)
    while not prime(number):
        number += 1
    return number

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

myBinaryMessage = textToBinary("MATH")
myDecimalMessage = binToDec(myBinaryMessage)
print(myBinaryMessage)
decodedBinary = decToBin(myDecimalMessage)
message = binaryToText(decodedBinary)
print(message)

"""
p = randomPrime(48)
q = randomPrime(2)
print('p: ' + str(p))
print('q: ' + str(q))
n = p * q
print('n: ' + str(n))
e = 13
d = modinv(e, (p-1)*(q-1))
print('e: ' + str(e))
print('d :' + str(d))

message = 15211738
ciphertext = powerMod(message, e, n)
print('Ciphertext: ' + str(ciphertext))
decodedMessage = powerMod(ciphertext, d, n)
print('Decoded Message: ' + str(decodedMessage))
"""
