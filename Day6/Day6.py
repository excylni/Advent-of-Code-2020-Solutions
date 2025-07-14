with open('Anwsers.txt', 'r') as file:
    Data = file.read()
    Data = Data.split('\n')


group_list = []
group = []

for word in Data:
    if word == '':
        if group:
            group_list.append(group)
            group = []
    else:
        group.append(word)


total = 0
for group in group_list:
    counts = set(''.join(group))
    total += len(counts)

print(total)

# Part 2
total = 0
for group in group_list:
    sets = [set(person) for person in group]
    common = set.intersection(*sets)
    total += len(common)

print(total)
