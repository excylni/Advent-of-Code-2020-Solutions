with open('Day12.txt', 'r') as file:
    letter = []
    number = []
    commands = file.read().split()
    for i in range(len(commands)): 
        letter.append(commands[i][0])
        number.append(int(commands[i][1:]))

def instructor(letter,number):
    NS = 0 # y
    EW = 0 # x 
    directions = ['east','south','west','north']
    direction = 'east'

    for i in range(len(letter)):
        
        if letter[i] == 'L':
            idx = directions.index(direction)
            steps = number[i] // 90
            idx = (idx - steps) % 4 
            direction = directions[idx]

        if letter[i] == 'R':
            idx =  directions.index(direction)
            steps = number[i] // 90
            idx = (idx + steps) % 4 
            direction = directions[idx]

        if letter[i] == 'F':
            idx =  directions.index(direction)

            if idx == 0:
                EW += number[i]
            if idx == 1:
                NS -= number[i]
            if idx == 2:
                EW -= number[i]
            if idx == 3:
                NS += number[i]


        if letter[i] == 'N':
            NS += number[i]
        if letter[i] == 'S':
            NS -= number[i]
        if letter[i] == 'E':
            EW += number[i]
        if letter[i] == 'W':
            EW -= number[i]

    distance = abs(NS) + abs(EW)
    
    return distance
