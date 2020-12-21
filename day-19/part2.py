import re
from copy import deepcopy

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


def special_matching_rules(regex, rule):
    modified_rule_8 = re.sub(f"^8(?=\D)|\D8(?=\D)| 8$", "x", rule)
    modified_rule_11 = re.sub(f"^11(?=\D)| 11(?=\D)| 11$", "y", modified_rule_8)
    if (match_rules(8, rule) or match_rules(11, rule)) or not re.search(regex, modified_rule_11):
        return True
    else:
        return False


def all_rules_parsed(rules):
    for rule in rules.values():

        if special_matching_rules(regex, rule):
            # print(f"The only number in {rule} is either 8 or 11")
            pass

        elif re.search(regex, rule):
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


def match_rules(p, rules_p):
    R = re.compile(f"^{p}\D|\D{p}\D|\D{p}$")
    # print(f"{R} --->  {rules_p}")
    return re.search(R, rules_p)


def make_rules(rules_list):
    cycle_count = 0
    rules = {}
    for rule in rules_list:
        id, rest = rule.split(":")
        rest = rest.replace('"', "").replace(" |", "|")
        if rest in [" a", " b"]:
            rules[id] = rest.replace(" ", "")
        else:
            rules[id] = rest
    regex_rules = deepcopy(rules)
    parsed = find_ab(rules)
    while not all_rules_parsed(rules):
        for idx, rule in rules.items():
            if idx not in parsed:
                print(f"looking at idx {idx}... cycle count: {cycle_count}")

                print(len(rules.keys()), len(parsed))

                for p in parsed:
                    if match_rules(p, rules[idx]):
                        # if idx == "11":
                        #     import pdb

                        #     pdb.set_trace()
                        # print(f"will replace rule {p} with {regex_rules[p]} in rule {rules[idx]}")
                        # rule = rule.replace(f" {p}", regex_rules[p])
                        rule = re.sub(f"^ {p}(?=\D)| {p}(?=\D)| {p}$", regex_rules[p], rule)
                        rules[idx] = rule
                        if special_matching_rules(regex, rule):
                            print(f"{rule} IS FULLY PARSED - idx {idx}")
                            regex_rules[idx] = f"({rule})"
                            parsed.append(idx)
                            print(f"----------------> {cycle_count}")
                            print(f" ALL RULES PARSED: {all_rules_parsed(rules)}")
                            print(f" PARSED CONTAINS ALL: {len(rules.keys()) == len(parsed)}")

                            break
    while cycle_count < 10:
        p = "8"
        temp = deepcopy(regex_rules[p])
        regex_rules[p] = re.sub(f"^ {p}(?=\D)| {p}(?=\D)| {p}$", regex_rules[p], temp)
        p = "11"
        temp = deepcopy(regex_rules[p])
        regex_rules[p] = re.sub(f"^ {p}(?=\D)| {p}(?=\D)| {p}$", regex_rules[p], temp)
        cycle_count += 1

    regex_rules["0"] = re.sub(f"^ 8(?=\D)| 8(?=\D)| 8$", regex_rules["8"], regex_rules["0"])
    regex_rules["0"] = re.sub(f"^ 11(?=\D)| 11(?=\D)| 11$", regex_rules["11"], regex_rules["0"])
    # print(regex_rules["0"])
    print(f"WHILE LOOP WILL STOP BECAUSE CYCLE COUNT IS {cycle_count}")
    return f"^{regex_rules['0']}$"


if __name__ == "__main__":
    rules_list, test_input = read_input("example2.txt")
    rules = make_rules(rules_list)
    count = 0
    print("NOW TESTING INPUT")
    print(len(rules))
    print(rules)
    # for input in test_input:
    #     if re.match(rules, input):
    #         print(f"{input} matches!!")
    #         count += 1
    # print(count)

