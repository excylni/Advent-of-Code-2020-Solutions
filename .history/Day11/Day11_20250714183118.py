with open('Day11.txt', 'r') as file:
    seats = file.read().splitlines()


def reader(seats):
    occupied = '#'
    occupied_seats = 0
    row, column = len(seats), len(seats[0])
    seats = [list(a) for a in seats]
    new_seats = [a.copy() for a in seats]

    for i in range(row):
        for j in range(column):

            if seats[i][j] == 'L':
                if all(
                        0 > i + dr or i + dr >= row or
                        0 > j + dc or j + dc >= column or
                        seats[i + dr][j + dc] != '#'
                        for dr in [-1, 0, 1]
                        for dc in [-1, 0, 1]
                        if not (dr == 0 and dc == 0)
                ):
                    new_seats[i][j] = '#'
            
            if seats[i][j] == '#':
                count = 0

                for dc in [-1, 0, 1]:
                    for dr in [-1, 0, 1]:

                        if dr == 0 and dc == 0: continue

                        nr, nc = i + dr, j + dc
                        if 0 <= nr < row and 0 <= nc < column:
                            if seats[nr][nc] == occupied:
                                count += 1

                            if count >= 4:
                                new_seats[i][j] = 'L'

    occupied_seats = sum(row.count(occupied) for row in new_seats)

    return new_seats, occupied_seats


prev_seats = None
current_seats = seats

while prev_seats != current_seats:
    prev_seats = current_seats
    current_seats, occupied_seats = reader(prev_seats)

print(occupied_seats)


# Part 2


def first_seen(seats, i, j, dr, dc, row, column):
    nr, nc = i + dr, j + dc
    while 0 <= nr < row and 0 <= nc < column:
        if seats[nr][nc] == '#':
            return True
        if seats[nr][nc] == 'L':
            return False
        nr += dr
        nc += dc
    return False


def new_reader(seats):
    occupied = '#'
    occupied_seats = 0
    row, column = len(seats), len(seats[0])
    seats = [list(a) for a in seats]
    new_seats = [a.copy() for a in seats]

    for i in range(row):
        for j in range(column):

            if seats[i][j] == 'L':
                if all(
                        0 > i + dr or i + dr >= row or
                        0 > j + dc or j + dc >= column or
                        not first_seen(seats, i, j, dr, dc, row, column)
                        for dr in [-1, 0, 1]
                        for dc in [-1, 0, 1]
                        if not (dr == 0 and dc == 0)
                ):
                    new_seats[i][j] = '#'

            if seats[i][j] == '#':
                count = 0

                for dc in [-1, 0, 1]:
                    for dr in [-1, 0, 1]:

                        if dr == 0 and dc == 0: continue

                        nr, nc = i + dr, j + dc
                        while 0 <= nr < row and 0 <= nc < column:
                            if seats[nr][nc] == occupied:
                                count += 1
                                break

                            elif seats[nr][nc] == 'L':
                                break

                            nr += dr
                            nc += dc

                        if count >= 5:
                            new_seats[i][j] = 'L'

    occupied_seats = sum(row.count(occupied) for row in new_seats)

    return new_seats, occupied_seats


prev_seats = None
current_seats = seats

while prev_seats != current_seats:
    prev_seats = current_seats
    current_seats, occupied_seats = new_reader(prev_seats)

print(occupied_seats)
