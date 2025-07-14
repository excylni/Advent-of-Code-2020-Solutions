with open('Anwsers.txt','r') as file:
    Anwsers = file.read()
    Anwsers = Anwsers.split('\n\n')
total = 0


for group in Anwsers:
    counts = group.replace('\n','')
    counts = {char for char in counts if char.isalpha()}
    
    total += len(counts)
