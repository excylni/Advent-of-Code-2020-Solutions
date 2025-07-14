with open('Day13.txt', 'r') as file:
    data = file.read()
    data = data.split()
    earliest_time = int(data[0])
    data_times = data[1].split(',')

bus_times = [int(a) for a in data_times if a != 'x']

earliest_departures = []

for i in bus_times:
    departure = ((earliest_time // i) + 1) * i

    earliest_departures.append(departure)

E = min(earliest_departures)
index = earliest_departures.index(E)

solution = (abs(earliest_time - E) * bus_times[index])
print(solution)


# Part 2

busses = [(int(i), int(v)) for i, v in enumerate(data_times) if v != 'x']

time = 0
step = 1

for offset, bus in busses:
    while (time + offset) % bus != 0:
        time += step
    step *= bus

print(time)
        
