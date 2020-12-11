import copy
import sys
from pprint import pprint


def read_input(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(list(line.replace("\n", "")))
    return data


def process_steps(data):
    temp_step = copy.deepcopy(data)
    print_layout(temp_step)
    for row_idx, row in enumerate(data):
        for seat_idx, seat in enumerate(row):
            new_seat = check_seat_part2(data, row_idx, seat_idx, seat)
            temp_step[row_idx][seat_idx] = new_seat
    return temp_step


def check_seat(data, x, y, seat_status):
    seats_occupied = 0
    if seat_status == ".":
        return "."
    # print(f"checking {x,y} which is currently {seat_status}")

    for (a, b) in (
        (x - 1, y),
        (x + 1, y),
        (x, y - 1),
        (x, y + 1),
        (x - 1, y - 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
    ):
        if a < 0 or b < 0:
            continue
        try:
            if data[a][b] == "#":
                seats_occupied += 1
        except IndexError:
            pass
        # print(f"checking outside bounds {a,b}")

    if seat_status == "#" and seats_occupied >= 4:
        return "L"

    elif seat_status == "L" and seats_occupied == 0:
        return "#"
    return seat_status


def find_first_seat_x(x=None, y=None, step=None, data=None):
    while x + step >= 0 and x + step < len(data):
        x = x + step
        if data[x][y] != ".":
            return x


def find_first_seat_y(x=None, y=None, step=None, data=None):
    while y + step >= 0 and y + step < len(data[0]):
        y = y + step
        if data[x][y] != ".":
            return y


def find_first_seat_x_y(x=None, y=None, step_x=None, step_y=None, data=None):
    while x is not None or y is not None:
        if x + step_x >= 0 and x + step_x < len(data):
            x = x + step_x
        else:
            return (None, y)
        if y + step_y >= 0 and y + step_y < len(data[0]):
            y = y + step_y
        else:
            return (x, None)

        if data[x][y] != ".":
            return x, y


def check_seat_part2(data, x, y, seat_status):
    seats_occupied = 0
    if seat_status == ".":
        return "."

    seats_around = (
        (find_first_seat_x(x, y, -1, data), y),
        (find_first_seat_x(x, y, 1, data), y),
        (x, find_first_seat_y(x, y, -1, data)),
        (x, find_first_seat_y(x, y, 1, data)),
        find_first_seat_x_y(x, y, -1, -1, data),
        find_first_seat_x_y(x, y, 1, 1, data),
        find_first_seat_x_y(x, y, 1, -1, data),
        find_first_seat_x_y(x, y, -1, 1, data),
    )

    for (a, b) in seats_around:
        if a is None or b is None or a < 0 or b < 0:
            continue
        try:
            if data[a][b] == "#":
                seats_occupied += 1
        except IndexError:
            pass

    if seat_status == "#" and seats_occupied >= 5:
        return "L"

    elif seat_status == "L" and seats_occupied == 0:
        return "#"
    return seat_status


def print_layout(data):
    print("\n".join(["".join(i) for i in data]))
    print()


if __name__ == "__main__":
    data = read_input("input.txt")
    while True:
        new_data = process_steps(data)
        if new_data == data:
            break
        data = copy.deepcopy(new_data)
    print("".join(["".join(i) for i in new_data]).count("#"))
