import pygal

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

counter = [0] * 26

def freqcount(text):
    text = text.upper().replace(' ','')
    
    for i in text:
        if i in LETTERS:
            position = LETTERS.find(i)
            counter[position] += 1
            
    return counter

def barchart(text, filename):
    text = text.upper().replace(' ','')
    line_chart = pygal.Bar()
    line_chart.title = 'Frequency Distribution of Text'
    line_chart.x_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    line_chart.add("Ciphertext", freqcount(text))
    line_chart.render_to_file(filename)
    return

def IC(text):
    text = text.upper().replace(' ','')
    index = 0
    length = len(text)
    frequency = 0
    probabilities = [0] * 26

    freqcount(text)
    
    for i in range(0, 26):
        frequency = counter[i]
        probabilities[i] = (frequency/length) * ((frequency - 1)/(length - 1))

    index = sum(probabilities)
    return index

def splitter(text, num):
    text = text.upper().replace(' ','')
    cleanedtext = ''
    for i in text:
        if i in LETTERS:
            cleanedtext += i
    text = cleanedtext
    piles = [None] * num
    position = 0

    for i in range(0, len(text)):
        position = i % num

        piles[position] += text[i]
    
    return piles

def KeyApproximator(text):
    text = text.upper().replace(' ','')
    cleanedtext = ''
    for i in text:
        if i in LETTERS:
            cleanedtext += i
    text = cleanedtext
    key = 0
    n = len(text)
    
    key = (0.027 * n)/((n-1) * IC(text) - 0.038 * n + 0.065)

    return key
    
    
