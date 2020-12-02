import re

example = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
1-2 d: dddnvx
"""


def parse_row(row):
    if row == "":
        return 0
    policy_str, password = row.split(":")
    regex = parse_policy(policy_str)
    password = "".join(sorted([c for c in password])).replace(" ", "").replace("\n", "")

    match = re.match(regex, password)
    if match:
        return 1
    else:
        return 0


def parse_policy(policy):
    policy = policy.replace(":", "")
    groups = re.match(r"(?P<start>\d+)-(?P<end>\d+) (?P<char>[a-z]+)", policy).groups()

    regex = "^[^{2}]*{2}{{{0},{1}}}[^{2}]*$".format(*groups)
    return regex


def read_input():
    with open("input.txt") as f:
        data = f.readlines()
    return data


if __name__ == "__main__":
    count = 0

    data = read_input()

    # for row in example.split("\n"):
    for row in data:
        count += parse_row(row)

    print(count)
