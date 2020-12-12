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


def change_waypoint_direction(waypoint_directions, dir, num):
    turn = int(num / 90)
    if dir == "L":
        turn = turn * -1

    if turn in [1, -3]:
        return {
            "east": waypoint_directions["north"],
            "west": waypoint_directions["south"],
            "north": waypoint_directions["west"],
            "south": waypoint_directions["east"],
        }

    if turn in [2, -2]:
        return {
            "east": waypoint_directions["west"],
            "west": waypoint_directions["east"],
            "north": waypoint_directions["south"],
            "south": waypoint_directions["north"],
        }
    if turn in [3, -1]:
        return {
            "east": waypoint_directions["south"],
            "west": waypoint_directions["north"],
            "north": waypoint_directions["east"],
            "south": waypoint_directions["west"],
        }


def find_route_with_waypoint(data):
    ship_directions = {"east": 0, "west": 0, "north": 0, "south": 0}
    waypoint_directions = {"east": 10, "west": 0, "north": 1, "south": 0}
    for instr in data:
        dir, num = instr[0], int(instr[1:])
        if dir == "F":
            for d in ship_directions:
                ship_directions[d] += num * waypoint_directions[d]
        if dir == "N":
            waypoint_directions["north"] += num
        if dir == "E":
            waypoint_directions["east"] += num
        if dir == "S":
            waypoint_directions["south"] += num
        if dir == "W":
            waypoint_directions["west"] += num
        if dir in ["R", "L"]:
            waypoint_directions = change_waypoint_direction(waypoint_directions, dir, num)

        print(ship_directions)
        print(waypoint_directions)
        print()

    result_east = abs(ship_directions["east"] - ship_directions["west"])
    result_north = abs(ship_directions["south"] - ship_directions["north"])
    print(result_east + result_north)


if __name__ == "__main__":
    data = read_input("input.txt")
    find_route(data)
    find_route_with_waypoint(data)
