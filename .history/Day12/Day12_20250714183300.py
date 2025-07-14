with open('Day12.txt','r') as file:
    letter = []
    number = []
    commands = file.read().split()
    for i in range(len(commands)): 
        letter.append(commands[i][0])
        number.append(int(commands[i][1:]))
