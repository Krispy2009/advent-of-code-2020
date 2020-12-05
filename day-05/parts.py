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


if __name__ == "__main__":
    max_seat_id = 0
    data = read_input()
    for boarding_pass in data:
        row, column = parse_boarding_pass(boarding_pass)
        seat_id = (row * 8) + column
        if max_seat_id < seat_id:
            max_seat_id = seat_id
    print(f"Max SeatID: {max_seat_id}")
