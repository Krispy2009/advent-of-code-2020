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


if __name__ == "__main__":
    data = read_input("input.txt")
    find_joltage_steps(data)
