from collections import defaultdict


def read_input(filename):
    tiles = {}
    with open(filename) as f:
        curr_tile = None
        for line in f.read().splitlines():
            if line.startswith("Tile"):
                curr_tile = int(line[5:-1])
                tiles[curr_tile] = []
            elif line == "":
                continue
            else:
                tiles[curr_tile].append(line)
    return tiles


def get_edges_choices(tiles):
    tile_edges = defaultdict(set)
    for tile in tiles:
        temp_edge_1 = temp_edge_2 = ""
        tile_edges[tile].add(tiles[tile][0])
        tile_edges[tile].add(tiles[tile][9])
        tile_edges[tile].add(tiles[tile][0][::-1])
        tile_edges[tile].add(tiles[tile][9][::-1])
        for row in tiles[tile]:
            temp_edge_1 += row[0]
            temp_edge_2 += row[9]
        tile_edges[tile].add(temp_edge_1)
        tile_edges[tile].add(temp_edge_2)
        tile_edges[tile].add(temp_edge_1[::-1])
        tile_edges[tile].add(temp_edge_2[::-1])

    return tile_edges


def find_matches(tile_edges):
    matches = defaultdict(list)
    for tile in tile_edges:
        for tile2 in tile_edges:
            if len(tile_edges[tile].intersection(tile_edges[tile2])) > 0:
                if tile != tile2:
                    matches[tile].append(tile2)

    return matches


def find_ans_part1(matches):
    ans = 1
    for match in matches:
        if len(matches[match]) == 2:
            print(f"Corner found: {match}")
            ans *= match
    print(f"Part 1: {ans}")


if __name__ == "__main__":
    tiles = read_input("input.txt")
    tile_edges = get_edges_choices(tiles)
    matches = find_matches(tile_edges)
    find_ans_part1(matches)
