with open('Day8.txt', 'r') as file:
    commands = file.read()
    commands = commands.split('\n')

commands_list = []

for command in commands:
    command = command.split()
    command[1] = int(command[1])
    commands_list.append(command)


def console(commands_list):
    accumulator = 0
    position = 0
    visited = set()

    while position < len(commands_list):
        if position in visited:
            break
        visited.add(position)

        operator, arg = commands_list[position]

        if operator == 'nop':
            position += 1
        if operator == 'acc':
            accumulator += arg
            position += 1
        if operator == 'jmp':
            position+= arg


    return accumulator, position

accumulator, position = console(commands_list)
print(accumulator)

# Part 2

import copy

def anti_corruption(commands_list):
    position = 0
    
    for i in range(len(commands_list)):
        modified = copy.deepcopy(commands_list)

        if modified[i][0] == 'acc':
            continue

        modified[i][0] = 'jmp' if modified[i][0] == 'nop' else 'nop'

        accumulator, position = console(modified)

        if position == (len(commands_list)):
            return accumulator, position

    return None, None


accumulator = anti_corruption(commands_list)
print(accumulator)
