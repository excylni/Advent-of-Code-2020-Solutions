from itertools import product
from collections import Counter

with open('Day17.txt', 'r') as file:
    grid = [line.strip() for line in file.readlines()]
    x = len(grid[0])
    y = len(grid)

    active_cubes = set()
    for y_i, row in enumerate(grid):
        for x_i, cell in enumerate(row):
            if cell == '#':
                active_cubes.add((x_i, y_i, 0))


def neighbour_checker(active_cubes):
    neighbours = [
        (dx, dy, dz)
        for dx, dy, dz in product([-1, 0, 1], repeat=3)
        if (dx, dy, dz) != (0, 0, 0)
    ]

    counts = Counter()
    for cube in active_cubes:
        x, y, z = cube

        for dx, dy, dz in neighbours:
            neighbour = (x + dx, y + dy, z + dz)
            counts[neighbour] += 1

    return counts


def transformer(active_cubes):
    changing_cells = neighbour_checker(active_cubes)
    new_active_cells = set()

    for cell, count in changing_cells.items():
        if cell in active_cubes:
            if count == 2 or count == 3:
                new_active_cells.add(cell)

        else:
            if count == 3:
                new_active_cells.add(cell)

    return new_active_cells


for i in range(6):
    active_cubes = transformer(active_cubes)

print(len(active_cubes))


# For part 2 we slightly change our code
active_cubes = set()

for y_i, row in enumerate(grid):
    for x_i, cell in enumerate(row):
        if cell == '#':
            active_cubes.add((x_i, y_i, 0, 0))


def neighbour_checker_4d(active_cubes):
    neighbours = [
        (dx, dy, dz, dw)
        for dx, dy, dz, dw in product([-1, 0, 1], repeat=4)
        if (dx, dy, dz, dw) != (0, 0, 0, 0)
    ]

    counts = Counter()
    for cube in active_cubes:
        x, y, z, w = cube

        for dx, dy, dz, dw in neighbours:
            neighbour = (x + dx, y + dy, z + dz, w + dw)
            counts[neighbour] += 1

    return counts


def transformer_4d(active_cubes):
    changing_cells = neighbour_checker_4d(active_cubes)
    new_active_cells = set()

    for cell, count in changing_cells.items():
        if cell in active_cubes:
            if count == 2 or count == 3:
                new_active_cells.add(cell)

        else:
            if count == 3:
                new_active_cells.add(cell)

    return new_active_cells


for i in range(6):
    active_cubes = transformer_4d(active_cubes)

print(len(active_cubes))