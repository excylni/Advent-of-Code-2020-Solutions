with open('Day13.txt', 'r') as file:
    data = file.read()
    data = data.split()
    earliest_time = int(data[0])
    data_times = data[1].split(',')