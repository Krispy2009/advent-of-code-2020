import re

parenthesis_re = re.compile(r"\(([^()]+)\)")


def read_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


def calculate(problem):
    parts = problem.split()
    total = int(parts[0])

    for p in range(1, len(parts), 2):
        if parts[p] == "*":
            total *= int(parts[p + 1])
        elif parts[p] == "+":
            total += int(parts[p + 1])
    return total


def solve_problem(problem):
    total = 0

    match = re.search(parenthesis_re, problem)
    while match:
        res = 0
        groups = match.groups()
        res += calculate(groups[0])
        problem = problem.replace(f"({groups[0]})", str(res))
        match = re.search(parenthesis_re, problem)

    else:
        # print(f"no parenthesis found in {problem}")
        total += calculate(problem)

    return total


if __name__ == "__main__":
    result = 0
    homework = read_input("input.txt")
    for problem in homework:
        res = solve_problem(problem)
        # print(f"****** {problem} = {res}")
        result += res

    print(result)
