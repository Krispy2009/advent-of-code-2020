import re

bag_re = re.compile(r"(?P<bag>.*) bags contain(?P<contents>.*)\.")
contents_re = re.compile(r"(?P<num>\d+) (?P<bag>.*) bag[s]?")


class Bag:
    def __init__(self, colour):
        self.colour = colour
        self.contents = []

    def add_content(self, contents):
        self.contents = contents

    def __str__(self):
        print(f"Bag: {self.colour}")


def read_input(filename):
    data = {}
    with open(filename, "r") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            bag, contents = re.match(bag_re, line).groups()
            bag = Bag(bag)
            bag.add_content(parse_contents(contents))
            data[bag.colour] = bag.contents

    return data


def parse_contents(contents):
    result = []
    contents = contents.split(",")
    for c in contents:
        c = c.strip()
        match = re.match(contents_re, c)
        if match:
            num, bag = match.groups()
            result.append((num, bag))
    return result


def count_bags(data):
    count, prev_count = 0, 0
    result_bags = set(["shiny gold"])
    new_result_bags = set()

    while True:
        prev_count = count
        result_bags = find_contents(result_bags, new_result_bags, data)
        new_result_bags = find_contents(new_result_bags, result_bags, data)
        count = len(new_result_bags | result_bags)

        if count == prev_count:
            print(len(new_result_bags | result_bags))
            break


def find_contents(bags, new_bags, data):
    new_bags = set(list(new_bags))
    for (bag, contents) in data.items():
        for result_bag in bags:
            for content in contents:
                if result_bag in content[1]:
                    new_bags.add(bag)
    return new_bags


def count_contents(data):
    checked_bags = ["shiny gold"]
    for colour in checked_bags:
        contents = data[colour]
        for content in contents:
            no_of_bags = int(content[0])
            for _ in range(no_of_bags):
                checked_bags.append(content[1])
    print(len(checked_bags) - 1)


if __name__ == "__main__":
    data = read_input("input.txt")
    count_bags(data)
    count_contents(data)
