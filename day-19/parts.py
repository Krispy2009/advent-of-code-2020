import re

EXAMPLE = """
0: 1 2
1: "a"
2: 1 3 | 3 1
3: "b"
"""
regex = re.compile(r"[ \d]+")


def read_input(filename):
    rules = []
    test_input = []
    read_rules = False
    with open(filename) as f:
        for line in f.read().splitlines():
            if line == "":
                read_rules = True
                continue
            if not read_rules:
                rules.append(line)
            else:
                test_input.append(line)
    return rules, test_input


def all_rules_parsed(rules):
    for rule in rules.values():
        if re.search(regex, rule):
            return False
    return True


def find_ab(rules):
    a, b = None, None
    for k, v in rules.items():
        if v == "a":
            a = k
        if v == "b":
            b = k
        if None not in [a, b]:
            break
    return [a, b]


def make_rules(rules_list):
    rules = {}
    for rule in rules_list:
        id, rest = rule.split(":")
        rest = rest.replace('"', "").replace(" |", "|")
        if rest in [" a", " b"]:
            rules[id] = rest.replace(" ", "")
        else:
            rules[id] = rest
    print(rules)
    parsed = find_ab(rules)
    while not all_rules_parsed(rules):
        print("not all parsed!")
        for idx, rule in rules.items():
            if idx not in parsed:
                for p in parsed:
                    print(f"will replace rule {p} with {rules[p]} in rule {rules[idx]}")
                    rule = rule.replace(f" {p}", rules[p])
                    rules[idx] = rule
                    print(rules)
                    print(parsed)
                    if not re.search(regex, rule):
                        print(f"{rule} IS FULLY PARSED")
                        parsed.append(idx)
                        break
    return rules


if __name__ == "__main__":
    rules_list, test_input = read_input("example.txt")
    print(rules_list)
    rules = make_rules(rules_list)
    print(rules)

