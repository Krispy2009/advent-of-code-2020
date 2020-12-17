import re
from collections import defaultdict

key_re = re.compile(r"(?P<field>.*): (?P<range1>.*) or (?P<range2>.*)\n")


def read_input(filename):
    key = {}
    nearby_tickets = []
    your_ticket = []
    read_your_ticket = False
    read_nearby_tickets = False
    with open(filename) as f:
        for line in f.readlines():
            match = re.match(key_re, line)
            if match:
                field, range1, range2 = match.groups()
                r1 = range1.split("-")
                r2 = range2.split("-")
                valid_numbers = list(range(int(r1[0]), int(r1[1]) + 1)) + list(
                    range(int(r2[0]), int(r2[1]) + 1)
                )
                key[field] = valid_numbers
            elif line.startswith("your"):
                read_your_ticket = True
            elif line.startswith("nearby"):
                read_nearby_tickets = True
            elif read_nearby_tickets:
                nearby_tickets.append([int(i) for i in line.replace("\n", "").split(",")])
            elif read_your_ticket:
                your_ticket = [int(i) for i in line.replace("\n", "").split(",")]
                read_your_ticket = False

    return key, your_ticket, nearby_tickets


def process_tickets(key, tickets):
    valid_values = set([value for values in key.values() for value in values])
    error_rate = 0
    invalid_tickets = []
    for idx, ticket in enumerate(tickets):
        t = set(ticket)
        difference = t.difference(valid_values)
        if difference:
            error_rate += sum(difference)
            invalid_tickets.append(idx)
    return error_rate, invalid_tickets


def compare_lists(column, field):
    return not set(column).difference(set(field))


def discover_fields(key, tickets):
    columns = map(list, zip(*tickets))
    fields = defaultdict(list)
    for idx, col in enumerate(columns):
        for field_name, field_value in key.items():
            if compare_lists(col, field_value):
                fields[field_name].append(idx)

    fields = filter_fields(fields)
    return fields


def filter_fields(fields):

    filtered_fields = {}

    while len(filtered_fields) != len(fields):
        for field in fields:
            if len(fields[field]) == 1 and field not in filtered_fields:
                filtered_fields[field] = fields[field][0]
                print(filtered_fields)
                for val in fields.values():
                    if len(fields[field]) and len(val) != 1 and fields[field][0] in val:
                        val.remove(fields[field][0])

    return filtered_fields


def parse_my_ticket(fields, ticket):
    result = 1
    for field in fields:
        if field.startswith("departure"):
            print(f"{field} : {ticket[fields[field]]}")

            result *= ticket[fields[field]]
    print(f"Result: {result}")


if __name__ == "__main__":
    key, your_ticket, nearby_tickets = read_input("input.txt")
    error_rate, invalid_tickets = process_tickets(key, nearby_tickets)
    print(f"Error rate: {error_rate}")
    valid_tickets = []
    for idx, ticket in enumerate(nearby_tickets):
        if idx not in invalid_tickets:
            valid_tickets.append(ticket)
    valid_tickets.append(your_ticket)

    fields = discover_fields(key, valid_tickets)
    parse_my_ticket(fields, your_ticket)
