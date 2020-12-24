from collections import defaultdict

DIRECTIONS = {"e": (1, 0), "se": (1, -1), "sw": (0, -1), "w": (-1, 0), "nw": (-1, 1), "ne": (0, 1)}

TILE_COUNTS = defaultdict(int)


def read_input(filename):
    instructions = []
    with open(filename) as f:
        for line in f.read().splitlines():
            line = parse_line(line)
            instructions.append(line)

    return instructions


def parse_line(line):
    parsed_line = []
    while line != "":
        char = line[0]
        if char in DIRECTIONS.keys():
            parsed_line.append(char)
            line = line[1:]
        else:
            char = line[0:2]
            if char in DIRECTIONS.keys():
                parsed_line.append(char)
                line = line[2:]
    return parsed_line


def apply_instructions(instructions):
    for instr in instructions:
        ref_tile = [0, 0]
        for step in instr:
            ref_tile[0], ref_tile[1] = (
                ref_tile[0] + DIRECTIONS[step][0],
                ref_tile[1] + DIRECTIONS[step][1],
            )
        TILE_COUNTS[tuple(ref_tile)] += 1


def find_black_tiles():
    black_tiles = 0
    for count in TILE_COUNTS.values():
        if count % 2 != 0:
            black_tiles += 1
    print(f"There are {black_tiles} black tiles")


if __name__ == "__main__":
    instructions = read_input("input.txt")
    apply_instructions(instructions)
    find_black_tiles()
