def get_input():
    report = []
    with open("input.txt") as f:
        for row in f.readlines():
            report.append(int(row))
    return report


def calculate_sums_for_two(report):
    for x in report:
        for y in report[1:]:
            if x + y == 2020:
                return (x, y)


def calculate_sums_for_three(report):
    for x in report:
        for y in report[1:]:
            for z in report[2:]:
                if x + y + z == 2020:
                    return (x, y, z)


if __name__ == "__main__":
    report = get_input()
    x, y = calculate_sums_for_two(report)
    print(f"Part 1 Answer: {x*y}")
    x, y, z = calculate_sums_for_three(report)
    print(f"Part 2 Answer: {x*y*z}")
