with open('Numbers.txt', 'r') as file:
    numbers = file.read()
    numbers = numbers.split()
    numbers_int = list(map(int, numbers))

target_sum = 2020

for i in numbers_int:
    for j in numbers_int:
        if i + j == target_sum:
            N = i * j

print(f"Part 1 result: {N}")

for i in numbers_int:
    for j in numbers_int:
        for k in numbers_int:
            if i + j + k == target_sum: 
                M = i * j * k
print(f"Part 2 result: {M}")
