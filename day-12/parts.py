def read_input(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            data.append(line.replace("\n", ""))
    print(data)
    return data


def change_direction(facing, dir, num):
    dirs = ["east", "south", "west", "north"]
    facing_now_idx = dirs.index(facing)
    turn = int(num / 90)
    if dir == "L":
        turn = turn * -1
    idx_to_go = (facing_now_idx + turn) % 4
    print(f"Started at {facing}, turning {dir} {num} to face {dirs[idx_to_go]}")
    return dirs[idx_to_go]


def find_route(data):
    directions = {"east": 0, "west": 0, "north": 0, "south": 0}
    facing = "east"
    for instr in data:
        dir, num = instr[0], int(instr[1:])
        if dir == "F":
            directions[facing] += num
        if dir == "N":
            directions["north"] += num
        if dir == "E":
            directions["east"] += num
        if dir == "S":
            directions["south"] += num
        if dir == "W":
            directions["west"] += num
        if dir in ["R", "L"]:
            facing = change_direction(facing, dir, num)

        print(directions)
    result_east = abs(directions["east"] - directions["west"])
    result_north = abs(directions["south"] - directions["north"])
    print(result_east + result_north)


if __name__ == "__main__":
    data = read_input("input.txt")
    find_route(data)
