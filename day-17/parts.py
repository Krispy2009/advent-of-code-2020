from collections import defaultdict


def read_input(filename):
    data = set()
    with open(filename) as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, cube in enumerate(line):
                if cube == "#":
                    data.add((x, y, 0, 0))
    return data


def process(activated):
    for _ in range(6):
        active_counts = defaultdict(int)
        for cube in activated:
            for ix in (-1, 0, 1):
                for iy in (-1, 0, 1):
                    for iz in (-1, 0, 1):
                        for iw in (-1, 0, 1):
                            if ix == iy == iz == iw == 0:
                                continue
                            # These have an active cube next to them so they **may** get activated
                            # if the counts are following the rules
                            active_counts[
                                (cube[0] + ix, cube[1] + iy, cube[2] + iz, cube[3] + iw)
                            ] += 1

        new_activated = set()

        for cube in activated:

            # Currently activated cubes. Should they stay active?
            if active_counts[cube] in [2, 3]:
                new_activated.add(cube)
            # Previously inactive cubes (this includes some active ones but we added them above)
            for new_cube in active_counts:
                if active_counts[new_cube] == 3:
                    new_activated.add(new_cube)

        activated = new_activated

    print(f"Ans: {len(activated)}")


if __name__ == "__main__":
    data = read_input("input.txt")
    process(data)
