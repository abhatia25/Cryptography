import enigma
machine = enigma.enigma()
machine.setLeft(enigma.rotors[1], 0)
machine.setMiddle(enigma.rotors[3], 10)
machine.setRight(enigma.rotors[2], 18)
machine.setReflector(enigma.reflectors[0])
machine.setPlugboard(enigma.plugboard())
print(machine.operate('LNSLHWXAZYXRFBUDXZVHIQENLOQZMYHSHLRTIZPQCHQUPHSAYPHGHTXPIIMRVLEGOBNZUUCHHJUGVDUIQXIUGOAZHLDOXLWMQOUCMRUJCNFAJIERBRQEWXXHXLIDXNQEZDGYOAOZOUAAOPLCBAMFMKWMKBKQMOZMWDCQPAZWMUXOZJCIAIBSKYEAKASFMVTUXLVZOKBWLSNOLXROMTQKGWMILCNHQKDEBYRDBYXGPSTAWFFBYNDZFCEXWVUJPFQTWFKFZUORDMGDRFLEMSWJJWMNTWZHLZUSPGAHBLHBYYTVPPVEBWGPBRXLPBNFWNSUODUFTZQKLWTXORBCHBKKBISZVDEYVJSEEBUZYQZGMUWECGGXSPUEMDPIWBJZUMNODANRZFQTSGJNGDXNYZGJKYYKTJKNJOWITZFGQNPLFPFTQHPOPHZFFQXDBZCRMAMOSKGUVXOIARBQDESLWUANBFVAJFMMBZKCZHAPRSOPBGRSOIESCI'))