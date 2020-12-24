from blist import blist

example1 = "32415"
example2 = "389125467"
input = "284573961"

nodes_dict = {}


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, cups):
        self.head = None
        self.count = 0
        if cups is not None:
            node = Node(value=cups.pop(0))
            self.head = node
            self.count += 1
            nodes_dict[node.value] = node
            for cup in cups:
                node.next_cup = Node(value=cup)
                node = node.next_cup
                self.count += 1
                nodes_dict[node.value] = node
            node.next_cup = self.head
        print("finished making list")

    def find_node(self, value):
        # optimization y'all!
        return nodes_dict[value]

    def print_ans_part_1(self):
        node = self.find_node(1)
        nodes = []
        while str(node.value) not in nodes and len(nodes) < 100:
            nodes.append(str(node.value))
            node = node.next_cup
        print("------ Part 1 -------")
        print("".join(nodes[1:]))
        print("---------------------")

    def print_ans_part_2(self):
        node = self.find_node(1)
        n1 = node.next_cup
        n2 = n1.next_cup
        print("------ Part 2 -------")
        print(f"{n1} * {n2} = {n1.value * n2.value}")
        print("---------------------")

    def __repr__(self):
        node = self.head
        nodes = []
        while str(node.value) not in nodes and len(nodes) < 100:
            nodes.append(str(node.value))
            node = node.next_cup
        return " => ".join(nodes)


def play_game(cups, is_part_2=True):
    cups = [int(x) for x in cups]
    total_rounds = 100
    if is_part_2:
        cups.extend([i for i in range(10, 1_000_001)])
        total_rounds = 10_000_000
    game = LinkedList(cups)
    round = 1
    current_cup = game.head
    while round <= total_rounds:
        if round % (total_rounds * 0.1) == 0:
            print(f" -- move {round} --")
        # print(game)
        # print(f"current cup: ({current_cup.value})")
        pickup_1 = current_cup.next_cup
        pickup_2 = pickup_1.next_cup
        pickup_3 = pickup_2.next_cup
        after_pickup_3 = pickup_3.next_cup
        current_cup.next_cup = after_pickup_3
        # print(f"pick up: {pickup_1.value}, {pickup_2.value}, {pickup_3.value}")

        destination_val = current_cup.value - 1

        while (
            destination_val in [pickup_1.value, pickup_2.value, pickup_3.value]
            or destination_val < 1
        ):
            destination_val -= 1
            if destination_val < 1:
                destination_val = game.count

        destination = game.find_node(destination_val)
        # print(f"destination: {destination.value}")
        # print(destination.next_cup)

        after_destination = destination.next_cup

        destination.next_cup = pickup_1
        pickup_3.next_cup = after_destination
        current_cup = current_cup.next_cup
        round += 1
    if is_part_2:
        game.print_ans_part_2()
    else:
        game.print_ans_part_1()


import cProfile

if __name__ == "__main__":
    with cProfile.Profile() as pr:
        cups = play_game(input)
    pr.print_stats()
