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
print(group_list[:1])
for group in group_list:
    counts = set(''.join(group))
    total += len(counts)

print(total)