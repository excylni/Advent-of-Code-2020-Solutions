with open('Day8.txt','r') as file:
    commands = file.read()
    commands = commands.split('\n')

commands_list = []

for command in commands:
    command = command.split()
    command[1] = int(command[1])
    commands_list.append(command)