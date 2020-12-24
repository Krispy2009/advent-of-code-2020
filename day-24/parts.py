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
    black_tiles = set()
    for tile, count in TILE_COUNTS.items():
        if count % 2 != 0:
            black_tiles.add(tile)
    print(f"Part 1: There are {len(black_tiles)} black tiles")

    return black_tiles


def find_neighbours(tile):
    neighbours = set()
    for (x, y) in DIRECTIONS.values():
        neighbours.add((tile[0] + x, tile[1] + y))
    return neighbours


def simulate(tiles, days):

    for day in range(0, days + 1):
        white_tiles = set()
        black_tiles = tiles
        for tile in tiles:
            neighbours = find_neighbours(tile)
            for neighbour in neighbours:
                if neighbour not in black_tiles:
                    white_tiles.add(neighbour)

        to_white = set()
        for tile in black_tiles:
            neighbours = find_neighbours(tile)
            n = 0
            for ne in neighbours:
                if ne in black_tiles:
                    n += 1
            if n == 0 or n > 2:
                to_white.add(tile)

        to_black = set()
        for tile in white_tiles:
            neighbours = find_neighbours(tile)
            n = 0
            for ne in neighbours:
                if ne in black_tiles:
                    n += 1
            if n == 2:
                to_black.add(tile)

        tiles = black_tiles.difference(to_white).union(to_black)
        if day == 100:
            print(f"Part 2: Day {day}: {len(black_tiles)}")


if __name__ == "__main__":
    instructions = read_input("input.txt")
    apply_instructions(instructions)
    black_tiles = find_black_tiles()
    simulate(black_tiles, 100)
