with open('Day16.txt', 'r') as file:
    input = file.read().strip()
    input = input.split("\n\n")
    conditions = input[0]
    _, my_ticket = input[1].split(":")
    my_ticket = [int(num) for num in my_ticket.strip().split(',')]
    nearby_tickets = input[2].split('\n')[1:]
    nearby_tickets = [[int(num) for num in i.split(',')]
                      for i in nearby_tickets]

    conditions = conditions.split('\n')


def validator(conditions, nearby_tickets):
    ranges = []
    invalid_sum = 0
    invalid = []
    fields = {}

    for line in conditions:
        field, number = line.split(':')
        number = number.split(' or ')
        number = [[int(num) for num in i.split("-")] for i in number]

        interval_1 = range(number[0][0], number[0][1] + 1)
        interval_2 = range(number[1][0], number[1][1] + 1)

        ranges.append((interval_1, interval_2))
        fields[field] = (interval_1, interval_2)

    for ticket in nearby_tickets:
        for i in ticket:

            if not any(i in interval for pair in ranges for interval in pair):
                invalid_sum += i
                invalid.append(i)

    return invalid_sum, fields


invalid, fields = validator(conditions, nearby_tickets)
print(invalid)


def is_valid_value(value, fields):
    return any(value in r1 or value in r2 for r1, r2 in fields.values())


nearby_tickets = [
    ticket for ticket in nearby_tickets if all(is_valid_value(v, fields) for v in ticket)
]


def field_searcher(fields, nearby_tickets):
    columns = list(zip(*nearby_tickets))
    possible_fields = {}

    for index, column in enumerate(columns):
        possible_fields[index] = set()

        for field, (range1, range2) in fields.items():
            if all(value in range1 or value in range2 for value in column):
                possible_fields[index].add(field)

    possible_fields = {index: field.copy() for index,
                       field in possible_fields.items()}

    while any(len(fields) > 1 for fields in possible_fields.values()):
        progress_made = False

        for column, possible_field in list(possible_fields.items()):
            if len(possible_field) == 1:
                field = next(iter(possible_field))

                for other_column in possible_fields:
                    if other_column != column and field in possible_fields[other_column]:
                        possible_fields[other_column].discard(field)
                        progress_made = True

        if not progress_made:
            print("No progress made; breaking loop")
            break

    final_fields = {}
    for col, fields_set in possible_fields.items():
        if len(fields_set) == 1:
            final_fields[col] = next(iter(fields_set))
            
    departure_columns = []

    for column, field in final_fields.items():
        if "departure" in field:
            departure_columns.append(column)

    return final_fields, departure_columns


final_fields, departure_columns = field_searcher(fields, nearby_tickets)

product = 1
for column in departure_columns:
    product *= my_ticket[column]

print(product)
