from collections import defaultdict

example = [0, 3, 6]
example2 = [1, 3, 2]
example3 = [2, 1, 3]
example4 = [1, 2, 3]
example5 = [2, 3, 1]
example6 = [3, 2, 1]
example7 = [3, 1, 2]
input = [14, 1, 17, 0, 3, 20]


def play_game(numbers):
    stats = defaultdict(list)
    turn = 1
    last_number_checked = None
    for num in numbers:
        stats[num].append(turn)
        last_number_checked = num
        turn += 1
    while True:

        # print(f"Turn {turn}: {dict(stats)}")
        # print(f"last number checked: {last_number_checked}")
        num = last_number_checked
        if len(stats[last_number_checked]) == 1:
            num = 0
            # print(f"last num: {last_number_checked}.. num is now {num}")
            last_number_checked = num
            stats[num].append(turn)
            turn += 1
            # print()
            continue

        if num in stats:
            if len(stats[num]) + 1 >= 2:
                # print(
                #     f"Num {num} has been spoken before in turns {stats[num][-1]} and  {stats[num][-2]}"
                # )
                new_num = stats[num][-1] - stats[num][-2]
                # print(f"new number = {new_num}")
                stats[new_num].append(turn)
                last_number_checked = new_num
            else:
                stats[num].append(turn)
                last_number_checked = num

        else:
            stats[num] = [turn]
            last_number_checked = num
        turn += 1
        # print()
        if turn > 30_000_000:
            for nums, turns in stats.items():
                if 30_000_000 in turns:
                    print(nums)
            return


if __name__ == "__main__":
    play_game(input)
