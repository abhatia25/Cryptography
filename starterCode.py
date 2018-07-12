import enigma
#We need to get all size 3 ordered sublists from our list of rotors
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import itertools
def allRotorSettings(S,m):
    mylist = []
    for l in itertools.combinations(S, m):
        mylist.append(list(l))
    rotorConfigs = []
    for conf in mylist:
        permutes = itertools.permutations(conf)
        for p in permutes:
            rotorConfigs.append(list(p))
    return rotorConfigs

rotorConfigs = allRotorSettings([0,1,2,3,4], 3) #this is a list of all 60 possible rotor configurations (5*4*3)

for i in rotorConfigs:
    machine = enigma.enigma()
    machine.setLeft(enigma.rotors[0], i[0])
    machine.setMiddle(enigma.rotors[1], i[1])
    machine.setRight(enigma.rotors[2], i[2])
    machine.setReflector(enigma.reflectors[0])
    machine.setPlugboard(enigma.plugboard())

print(rotorConfigs)
