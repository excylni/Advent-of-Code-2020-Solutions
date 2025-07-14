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


def summer(numbers, invalid):
    for i in range(len(numbers)):
        for j in range(len(numbers)): 
            contigous_set = numbers[i:j+1]

            if sum(contigous_set) == invalid:

                min_val, max_val = min(contigous_set), max(contigous_set)
                sumz = contigous_set
                return min_val, max_val, sumz

    return None, None, []


min_val, max_val, contigous_set = summer(numbers, invalid)
print(min_val + max_val)