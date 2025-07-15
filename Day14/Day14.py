from itertools import product


mem = {}
mem2 = {}
mask = None


def apply_mask(value, mask):
    value = int(value)
    bin_value = bin(value)[2:].zfill(36)

    result = []
    for i, j in zip(bin_value, mask):
        if j == 'X':
            result.append(i)
        else:
            result.append(j)

    return int(''.join(result), 2)


def decoder(adress, mask):
    adress = int(adress)
    bin_adress = bin(adress)[2:].zfill(36)

    result = []
    for i ,j in zip(bin_adress, mask):
        if j == '1':
            result.append('1')
        elif j == 'X':
            result.append('X')
        elif j == '0':
            result.append(i)

    floating_bits = result.count('X')
    combinations = product('01', repeat=floating_bits)

    new_result = []
    for combo in combinations:
        temp = result.copy()
        combo_iter = iter(combo)

        for i in range(len(temp)):
            if temp[i] == 'X':
                temp[i] = next(combo_iter)

        new_result.append(int(''.join((temp)), 2))

    return new_result


with open('Day14.txt', 'r') as file:
    data = file.read().split('\n')
    for line in data:
        if line.startswith('mask'):
            _, mask = line.split('=')
            mask = mask.strip()
        else:
            left, value = line.split('=')
            adress = int(left[left.index('[') + 1: left.index(']')])

            mask_value = apply_mask(value, mask)
            mem[adress] = int(mask_value)

            mask_value2 = decoder(adress, mask)

            for i in mask_value2:
                mem2[i] = int(value)


print(f"Part1: {sum(mem.values())}")
print(f"Part2: {sum(mem2.values())}")
