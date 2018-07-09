import pygal

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def freqcount(text):
    
    counter = [0] * 26
    text = text.upper()
    
    for i in text:
        if i in LETTERS:
            position = LETTERS.find(i)
            counter[position] += 1
            
    return counter

def barchart(text, filename):
    line_chart = pygal.Bar()
    line_chart.title = 'Frequency Distribution of Text'
    line_chart.x_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    line_chart.add("Ciphertext", freqcount(text))
    line_chart.render_to_file(filename)
    return
