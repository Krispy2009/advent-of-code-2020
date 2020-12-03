example = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


def slide_down(course):
    if isinstance(course, str):
        course = course.split("\n")
    else:
        course = [row.replace("\n", "") for row in course]
    mod = len(course[0])
    x, y = 0, 0
    count = 0
    for row in course:
        row = row.replace("\n", "")
        y += 1
        if y == 1:
            continue
        x += 3
        print(row, x % mod)
        if row[x % mod] == "#":
            count += 1
        if y == len(course):
            break
    return count


def read_input():
    with open("input.txt", "r") as f:
        data = f.readlines()

    return data


if __name__ == "__main__":
    data = read_input()
    # print(f"{slide_down(example)}")
    print(f"{slide_down(data)}")

