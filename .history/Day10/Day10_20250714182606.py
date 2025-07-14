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
            three += 1
        if dif == 1:
            one += 1

    return one, three


one, three = builder(numbers)
print(one * three)

# Part 2


def dp(numbers):
    numbers = sorted(numbers)
    dp = {0:1}

    for n in numbers[1:]:
        dp[n] = dp.get(n-3, 0) + dp.get(n-2, 0) + dp.get(n-1, 0)

    return dp[max(numbers)]


ways = dp(numbers)
print(ways)
