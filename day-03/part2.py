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


def slide_down(course, slope_x, slope_y):
    if isinstance(course, str):
        course = course.split("\n")
    else:
        course = [row.replace("\n", "") for row in course]
    mod = len(course[0])
    x, y = 0, 0
    count = 0
    for idx, row in enumerate(course):
        y += slope_y
        if (y == slope_y) or (idx % slope_y != 0):
            continue
        x += slope_x
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
    answers = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        answers.append(slide_down(data, slope[0], slope[1]))

    print(f"{answers}")
    result = 1
    for i in answers:
        result = result * i

    print(result)
