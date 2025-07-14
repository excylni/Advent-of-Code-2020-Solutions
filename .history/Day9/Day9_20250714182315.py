with open('Preamble.txt', 'r') as file:
    numbers = file.read().split('\n')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])


def calculator(numbers, preamble):
    position = preamble

    while position < len(numbers):
        start = position - preamble
        end = position
        found = False

        for i in range(start, end):
            for j in range(start, end):

                if i == j:
                    continue
                if numbers[end] == numbers[i] + numbers[j]:
                    found = True
                    break
            if found:
                break

        if not found:
            invalid = numbers[end]
            print(invalid)
        position += 1

    return invalid


invalid = calculator(numbers, 25)

# Part 2