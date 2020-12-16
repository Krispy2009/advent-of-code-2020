import re

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
    for ticket in tickets:
        t = set(ticket)
        difference = t.difference(valid_values)
        if difference:
            error_rate += sum(difference)
    return error_rate


if __name__ == "__main__":
    key, your_ticket, nearby_tickets = read_input("input.txt")
    error_rate = process_tickets(key, nearby_tickets)
    print(f"Error rate: {error_rate}")
