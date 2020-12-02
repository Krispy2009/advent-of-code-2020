import re

example = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


def parse_row(row):
    if row == "":
        return 0
    policy_str, password = row.split(":")
    start, end, char = parse_policy(policy_str)
    password = password.replace(" ", "").replace("\n", "")
    print(start, end, char)

    if password[int(start) - 1] == char:
        if password[int(end) - 1] == char:
            return 0
        else:
            return 1
    elif password[int(end) - 1] == char:
        return 1
    else:
        return 0


def parse_policy(policy):
    policy = policy.replace(":", "")
    return re.match(r"(?P<start>\d+)-(?P<end>\d+) (?P<char>[a-z]+)", policy).groups()


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
