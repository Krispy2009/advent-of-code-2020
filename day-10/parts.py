from collections import defaultdict


def read_input(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            num = int(line.replace("\n", ""))
            data.append(num)
    return data


def find_joltage_steps(data):
    # prepare adaptors
    data = [0] + sorted(data)
    data.append(max(data) + 3)

    print(data)
    joltage_steps = defaultdict(int)
    for idx, joltage in enumerate(data):
        if idx == len(data) - 1:
            print(joltage_steps)
            break
        step = data[idx + 1] - joltage
        if step <= 3:
            joltage_steps[step] += 1
    print(f"Answer: {joltage_steps[1] * joltage_steps[3]}")


def calculate_arrangements(data):
    # prepare adaptors
    data = [0] + sorted(data)
    # data.append(max(data) + 3)

    possible_choices = {}

    for jolt in data:
        valid_jolts = [jolt + 1, jolt + 2, jolt + 3]
        valid_jolts = [x for x in valid_jolts if x in data]
        possible_choices[jolt] = valid_jolts
    print(possible_choices)

    results = {0: 1}
    for adapter, choices in possible_choices.items():
        print(f"adapter: {adapter}")
        for choice in choices:
            if choice in results:
                results[choice] += results[adapter]
            else:
                results[choice] = results[adapter]
        print(results)
    print(results[max(results.keys())])


if __name__ == "__main__":
    data = read_input("example.txt")
    find_joltage_steps(data)
    calculate_arrangements(data)
