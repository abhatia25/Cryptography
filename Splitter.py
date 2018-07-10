from Tools import *

text = open('challenge03b.txt').read()
count = 0

for pile in splitter(text, 5):
    barchart(pile, "1_" + str(count) + '.svg')
    count += 1

