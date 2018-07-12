import enigma
plaintext = 'FORALLWHOAREREADINGTHISHELLOYOUHAVESOLVEDTHISCOMPLEXENIGMACIPHERWEHAVEUSEDASERIESOFTECHNIQUESTHATTHEAVERAGEPERSONWOULDNOTBECAPABLEOFDOINGWITHOUTTHEASSISTANCEOFOURWONDERFULTEACHERMRGIBSONANDOURTATHOMASWEHAVESPENTTHEWEEKOFJULYEIGHTHLEARNINGALLABOUTCIPHERSSUCHASTHEVIGENEREHILLCAESARANDENIGMADESPITEALLTHEUSEOFCRYPTOGRAPHYINTHEPASTITREMAINSAFASCINATINGSCIENCETHATPROVESTOBEFUNDAMENTALFORTHEFUTURE'
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = ''
plaintext.upper().replace(' ', '')
machine = enigma.enigma()
machine.setLeft(enigma.rotors[4], 0) 
machine.setMiddle(enigma.rotors[1], 10) 
machine.setRight(enigma.rotors[2], 18) 
machine.setReflector(enigma.reflectors[0]) 
a = enigma.plugboard()
a.connect('N', 'V')
a.connect('A', 'B')
a.connect('T', 'C')
a.connect('X', 'J')
a.connect('Q', 'E')
a.connect('M', 'F')
a.connect('K', 'G')
a.connect('R', 'D')
a.connect('W', 'H')
a.connect('O', 'Y')
a.connect('I', 'P')
a.connect('L', 'S')
a.connect('U', 'Z')
machine.setPlugboard(a)
ciphertext = machine.operate(plaintext)
print('Ciphertext: ' + ciphertext)

