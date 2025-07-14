with open('Day12.txt', 'r') as file:
    letter = []
    number = []
    commands = file.read().split()
    for i in range(len(commands)): 
        letter.append(commands[i][0])
        number.append(int(commands[i][1:]))


def instructor(letter, number):


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

distance = instructor(letter,number)
print(distance)

# Part 2

def new_instructor(letter,number):
    x, y = [10,1] # East, North -> x,y
    location = [0,0]
    directions = ['east','south','west','north']

    for i in range(len(letter)):
        
        if letter[i] == 'R':
            if number[i] == 90:
                x, y = y,-x
            elif number[i] == 180:
                x, y= -x,-y
            elif number[i] == 270:
                x, y = -y, x
            
            

        elif letter[i] == 'L':
            if number[i] == 90:
                x,y = [-y,x]
            elif number[i] == 180:
                x,y = [-x,-y]
            elif number[i] == 270:
                x,y = [y,-x]
            
            

        elif letter[i] == 'F':
           location[0] += number[i] * x
           location[1] += number[i] * y


        elif letter[i] == 'N':
            y += number[i]
        elif letter[i] == 'S':
            y -= number[i]
        elif letter[i] == 'E':
            x += number[i]
        elif letter[i] == 'W':
            x -= number[i]

        
        
    distance = abs(location[0]) + abs(location[1])
    
    return distance

distance = new_instructor(letter,number)
print(distance)