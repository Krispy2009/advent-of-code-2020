example = "BFFFBBFRRR"


def parse_boarding_pass(code):
    rows = list(range(128))
    columns = list(range(8))
    for char in code:

        if char == "F":
            rows = rows[: (len(rows) // 2)]
        if char == "B":
            rows = rows[len(rows) // 2 :]
        if char == "L":
            columns = columns[: len(columns) // 2]
        if char == "R":
            columns = columns[len(columns) // 2 :]

    return rows[0], columns[0]


def read_input():
    data = []
    with open("input.txt") as f:
        for line in f.readlines():
            data.append(line.replace("\n", ""))
    return data


def find_my_seat(seats):
    for seat in range(seats[0], len(seats)):
        if seat not in seats:
            print(f"My seat: {seat}")


if __name__ == "__main__":
    max_seat_id = 0
    all_seat_ids = []
    data = read_input()
    for boarding_pass in data:
        row, column = parse_boarding_pass(boarding_pass)
        seat_id = (row * 8) + column
        all_seat_ids.append(seat_id)
        if max_seat_id < seat_id:
            max_seat_id = seat_id
    print(f"Max SeatID: {max_seat_id}")

    find_my_seat(sorted(all_seat_ids))

