with open('Day10.txt', 'r') as file:
    numbers = file.read().split('\n')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

built_in_joltage = max(numbers) + 3 
numbers.append(built_in_joltage)
numbers = numbers + [0]


def builder(numbers):
    numbers = sorted(numbers)
    one = 0 
    three = 0 

    for i in range(len(numbers)-1):
        dif = numbers[i+1] - numbers[i]

        if dif == 3:
            three +=1
        if dif == 1:
            one+=1
    
    return one, three