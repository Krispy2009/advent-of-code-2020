def get_input():
    report = []
    with open("input.txt") as f:
        for row in f.readlines():
            report.append(int(row))
    return report


def calculate_sums(report):
    for x in report:
        for y in report[1:]:
            if x + y == 2020:
                return (x, y)


if __name__ == "__main__":
    report = get_input()
    x, y = calculate_sums(report)
    print(f"Answer: {x*y}")
