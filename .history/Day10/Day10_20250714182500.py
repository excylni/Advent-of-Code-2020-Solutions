with open('Day10.txt','r') as file:
    numbers = file.read().split('\n')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

built_in_joltage = max(numbers) + 3 
numbers.append(built_in_joltage)
numbers = numbers + [0]
