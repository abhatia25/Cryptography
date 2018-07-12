letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
class rotor:
    #map describes rotos, machine is a reference to an enigma machine
    def __init__(self, map):
        self.rmap = map
        self.invMap = {v: k for k, v in self.rmap.items()} #We invert the mapping for the return trip
        self.index = 0 #index descrives the rotor's position relative to the machines
        self.rotateCount = 0 #keeps track of how man times we have moved
    def setIndex(self, index):
        if (index >= 26):
            raise Exception("A rotor position must not be more than 25!")
        self.index = index
    def rotate(self):
        #Rotate our index relative to Enigma Machine
        self.index = (self.index + 1) % 26 #rotate
        self.rotateCount += 1
        #https://en.wikipedia.org/wiki/Enigma_machine#Turnover
        if not self.left is None and (self == rotors[0] and self.index == letters.index('R') or (self == rotors[1] and self.index == letters.index('F')) or (self == rotors[2] and self.index == letters.index('W')) or (self == rotors[3] and self.index == letters.index('K')) or (self == rotors[4] and self.index == letters.index('A'))):
            self.left.rotate() #Turnover

    #Passes signal to through me and to rotor to left
    def passLeft(self, input):
        out = letters.index(self.rmap[letters[(input - self.index) % 26]])
        if self.left is None:
            return self.passRight(self.reflector.reflect((out + self.index) % 26))
        return self.left.passLeft((out + self.index) % 26) #recursive call
    #Passes signal through me and to rotor to right
    def passRight(self, input):
        out = letters.index(self.invMap[letters[(input - self.index) % 26]])
        if self.right is None:
            return letters[(out + self.index) % 26]
        return self.right.passRight((out + self.index)% 26) #recursive call
    def setNeighbors(self, left, right):
        self.left = left
        self.right = right
    def setReflector(self, reflector):
        self.reflector = reflector
    #Perform reflection
    def reflect(self, input):
        return letters.index(self.rmap[letters[input]])
    def setPosition(self, num):
        self.index = num
        self.rotateCount = num #Does this get set to zero or to num? A specific engima rotor design question

rotorOne = rotor({'A': 'E', 'B' : 'K', 'C' : 'M', 'D': 'F', 'E' : 'L', 'F' : 'G', 'G' : 'D', 'H' : 'Q', 'I' : 'V', 'J' : 'Z', 'K' : 'N', 'L' : 'T', 'M' : 'O', 'N' : 'W', 'O' : 'Y', 'P' : 'H', 'Q' : 'X', 'R' : 'U', 'S' : 'S', 'T' : 'P', 'U' : 'A' , 'V' : 'I', 'W' : 'B', 'X' : 'R', 'Y' : 'C', 'Z' : 'J'})
rotorTwo = rotor({'A': 'A', 'B' : 'J', 'C' : 'D', 'D': 'K', 'E' : 'S', 'F' : 'I', 'G' : 'R', 'H' : 'U', 'I' : 'X', 'J' : 'B', 'K' : 'L', 'L' : 'H', 'M' : 'W', 'N' : 'T', 'O' : 'M', 'P' : 'C', 'Q' : 'Q', 'R' : 'G', 'S' : 'Z', 'T' : 'N', 'U' : 'P' , 'V' : 'Y', 'W' : 'F', 'X' : 'V', 'Y' : 'O', 'Z' : 'E'})
rotorThree = rotor({'A': 'B', 'B' : 'D', 'C' : 'F', 'D': 'H', 'E' : 'J', 'F' : 'L', 'G' : 'C', 'H' : 'P', 'I' : 'R', 'J' : 'T', 'K' : 'X', 'L' : 'V', 'M' : 'Z', 'N' : 'N', 'O' : 'Y', 'P' : 'E', 'Q' : 'I', 'R' : 'W', 'S' : 'G', 'T' : 'A', 'U' : 'K' , 'V' : 'M', 'W' : 'U', 'X' : 'S', 'Y' : 'Q', 'Z' : 'O'})
rotorFour = rotor({'A': 'E', 'B' : 'S', 'C' : 'O', 'D': 'V', 'E' : 'P', 'F' : 'Z', 'G' : 'J', 'H' : 'A', 'I' : 'Y', 'J' : 'Q', 'K' : 'U', 'L' : 'I', 'M' : 'R', 'N' : 'H', 'O' : 'X', 'P' : 'L', 'Q' : 'N', 'R' : 'F', 'S' : 'T', 'T' : 'G', 'U' : 'K' , 'V' : 'D', 'W' : 'C', 'X' : 'M', 'Y' : 'W', 'Z' : 'B'})
rotorFive = rotor({'A': 'V', 'B' : 'Z', 'C' : 'B', 'D': 'R', 'E' : 'G', 'F' : 'I', 'G' : 'T', 'H' : 'Y', 'I' : 'U', 'J' : 'P', 'K' : 'S', 'L' : 'D', 'M' : 'N', 'N' : 'H', 'O' : 'L', 'P' : 'X', 'Q' : 'A', 'R' : 'W', 'S' : 'M', 'T' : 'J', 'U' : 'Q' , 'V' : 'O', 'W' : 'F', 'X' : 'E', 'Y' : 'C', 'Z' : 'K'})
reflectorB = rotor({'A': 'Y', 'B' : 'R', 'C' : 'U', 'D': 'H', 'E' : 'Q', 'F' : 'S', 'G' : 'L', 'H' : 'D', 'I' : 'P', 'J' : 'X', 'K' : 'N', 'L' : 'G', 'M' : 'O', 'N' : 'K', 'O' : 'M', 'P' : 'I', 'Q' : 'E', 'R' : 'B', 'S' : 'F', 'T' : 'Z', 'U' : 'C' , 'V' : 'W', 'W' : 'V', 'X' : 'J', 'Y' : 'A', 'Z' : 'T'})
reflectorC = rotor({'A': 'F', 'B' : 'V', 'C' : 'P', 'D': 'J', 'E' : 'I', 'F' : 'A', 'G' : 'O', 'H' : 'Y', 'I' : 'E', 'J' : 'D', 'K' : 'R', 'L' : 'Z', 'M' : 'X', 'N' : 'W', 'O' : 'G', 'P' : 'C', 'Q' : 'T', 'R' : 'K', 'S' : 'U', 'T' : 'Q', 'U' : 'S' , 'V' : 'B', 'W' : 'N', 'X' : 'M', 'Y' : 'H', 'Z' : 'L'})
rotors = [rotorOne, rotorTwo, rotorThree, rotorFour, rotorFive]
reflectors = [reflectorB, reflectorC]


class enigma:
    def __init__(self):
        self.left = None
        self.middle = None
        self.right = None
        self.reflector = None
        self.plugboard = None
        self.invPlugboard = None
    def setLeft(self, rotor, position):
        self.left = rotor
        rotor.setPosition(position)
    def setMiddle(self, rotor, position):
        self.middle = rotor
        rotor.setPosition(position)
    def setRight(self, rotor, position):
        self.right = rotor
        rotor.setPosition(position)
    def setReflector(self, reflector):
        self.reflector = reflector
    def setPlugboard(self, plug):
        self.plugboard = plug
    def encodeChar(self, char):
        if (self.left == None or self.middle == None or self.right == None):
            raise Exception("You must specify left, middle, and right rotors!")
        if (self.plugboard == None):
            raise Exception("You must specify a plugboard configuration!")
        if len([self.left, self.middle, self.right]) != len(set([self.left, self.middle, self.right])):
            raise Exception("You cannot use two rotors twice!")
        char = char.upper()
        self.left.setNeighbors(None, self.middle)
        self.left.setReflector(self.reflector)
        self.middle.setNeighbors(self.left, self.right)
        self.right.setNeighbors(self.middle, None)

        plug = self.plugboard.mapping[char] #Send through plugboard

        out = self.right.passLeft(letters.index(plug)) #Kickoff rotor recursion
        out = self.plugboard.mapping[out] #Send back through plugboard
        self.right.rotate() #Rotate rightmost rotor once
        return out
    def operate(self, message):
        m = ''
        for c in message:
            m += self.encodeChar(c)
        return m
class plugboard:
    def __init__(self):
        self.mapping = {}
        for l in letters:
            self.mapping[l] = l
    def connect(self, a, b):
        a = a.upper()
        b = b.upper()
        if (self.mapping[a] != a or self.mapping[b] != b):
            raise Exception("Cannot connect to a letter that is already in a connection, disconnect first!")
        self.mapping[a] = b
        self.mapping[b] = a
    def disconnect(self, a, b):
        a = a.upper()
        b = b.upper()
        if self.mapping[a] != b or self.mapping[b] != a:
            raise Exception("Cannot disconnect a connection that doesn't exist!")
        self.mapping[a] = a
        self.mapping[b] = b
