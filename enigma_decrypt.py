import enigma
#We need to get all size 3 ordered sublists from our list of rotors
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import itertools
reflectors = [0, 1]
ciphertext = 'ZINC'
plaintext = ''
rotor1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
##rotor2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
##rotor3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
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

rotorConfigs = allRotorSettings([0,1,2,3,4], 1) #this is a list of all 60 possible rotor configurations (5*4*3)

ciphertext = ciphertext.upper().replace(' ','')

for i in rotorConfigs[:30]:
    for a in rotor1:
        #for b in rotor2:
            #for c in rotor3:
                for r in reflectors:
                    machine = enigma.enigma()
                    machine.setLeft(enigma.rotors[i[0]], a)
                    #machine.setMiddle(enigma.rotors[i[1]], b)
                    #machine.setRight(enigma.rotors[i[2]], c)
                    machine.setReflector(enigma.reflectors[r])
                    machine.setPlugboard(enigma.plugboard())
                    plaintext = machine.operate(ciphertext)
                    if 'THE' in plaintext and 'AND' in plaintext and 'FOR' in plaintext:
                        print(plaintext)
                        print('Left rotor: ' + str(i[0]) + ', ' + str(a))
                        print('Middle rotor: ' + str(i[1]) + ', ' + str(b))
                        print('Right rotor: ' + str(i[2]) + ', ' + str(c))
                        print('Reflector: ' + str(r))
