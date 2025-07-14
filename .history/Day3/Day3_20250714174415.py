with open('Trees.txt', 'r') as file:
    data = [line.strip() for line in file]

height = len(data)
lenght = len(data[1])

print(height, lenght)

right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]
trees_n = []

def counter(data, right, down):
    x = y = trees = 0

    while height > y:
        if data[y][x % lenght] == '#':
            trees+=1
        y += down[i]
        x += right[i]
    return trees_n.append(trees)

for i in range(len(right)):
    counter(data,right, down)

print(trees_n)

product =1 
for i in trees_n:
    product*=i
print(product)


