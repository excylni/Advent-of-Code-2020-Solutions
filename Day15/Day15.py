with open('Day15.txt', 'r') as file:
    numbers = file.read()
    numbers = numbers.split(',')
    numbers = [int(i) for i in numbers]


def memory_game(numbers):
    turn = 1
    spoken_number = []
    while turn < 2021:

        if turn in range(1, len(numbers) + 1):
            spoken_number.append(numbers[turn-1])
        else:
            last_number = spoken_number[-1]
            if spoken_number.count(last_number) < 2:
                spoken_number.append(0)
            else:
                indices = [i for i, x in enumerate(spoken_number) if x == last_number]
                difference = indices[-1] - indices[-2]
                spoken_number.append(difference)
        turn += 1
    return spoken_number[-1]


def better_memory_game(numbers, limit):
    last_seen = {number: turn + 1 for turn, number in enumerate(numbers[:-1])}
    last_number = numbers[-1]

    for turn in range(len(numbers), limit):
        if last_number in last_seen:
            new = turn - last_seen[last_number]
        else:
            new = 0

        last_seen[last_number] = turn
        last_number = new

    return last_number


spoken_number = memory_game(numbers)
last_number = better_memory_game(numbers, 30_000_000)
print(f" Part 1 result: {spoken_number}")
print(f" Part 2 result: {last_number}")