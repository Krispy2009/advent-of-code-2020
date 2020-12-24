example1 = "32415"
example2 = "389125467"
input = "284573961"


def play_game(cups):
    cups = [int(cup) for cup in cups]
    total_cups = len(cups)
    curr_cup_idx = 0
    current_cup = cups[curr_cup_idx]
    round = 1
    destination = cups[curr_cup_idx]
    while round <= 101:
        pickup = (
            (curr_cup_idx + 1) % total_cups,
            (curr_cup_idx + 2) % total_cups,
            (curr_cup_idx + 3) % total_cups,
        )
        print(f"\n-- move {round} --")
        cups_str = " ".join(f"({x})" if x == current_cup else str(x) for x in cups)
        print(f"cups: {cups_str}")
        pickup_1, pickup_2, pickup_3 = cups[pickup[0]], cups[pickup[1]], cups[pickup[2]]
        cups[pickup[0]], cups[pickup[1]], cups[pickup[2]] = 100, 100, 100  # to maintain space
        cups.remove(100)
        cups.remove(100)
        cups.remove(100)
        print(f"pick up: {pickup_1}, {pickup_2}, {pickup_3}")

        destination = current_cup
        while destination > 0:

            destination -= 1

            if destination in cups:
                break
            if destination == 0:
                valid_values = [i for i in cups if i != 100]
                destination = max(valid_values)
                break

        print(f"destination: {destination}")

        destination_idx = cups.index(destination)

        insert_idx_1 = (destination_idx + 1) % total_cups
        insert_idx_2 = (destination_idx + 2) % total_cups
        insert_idx_3 = (destination_idx + 3) % total_cups

        cups.insert(insert_idx_1, pickup_1)
        cups.insert(insert_idx_2, pickup_2)
        cups.insert(insert_idx_3, pickup_3)

        curr_cup_idx = cups.index(current_cup)
        curr_cup_idx = (curr_cup_idx + 1) % total_cups
        current_cup = cups[curr_cup_idx]
        round += 1


if __name__ == "__main__":
    play_game(input)
