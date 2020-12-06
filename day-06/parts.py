def read_input(filename):
    data = []
    full_group = ""
    with open(filename, "r") as f:
        for line in f.readlines():
            if line != "\n":
                line = line.replace("\n", "")
                full_group = f"{full_group}{line}"
            else:
                data.append(full_group)
                full_group = ""
        # add the last line
        data.append(full_group)
    return data


def count_answers(data):
    total = 0
    for line in data:
        unique_ans = set(line)
        total += len(unique_ans)
    print(total)


if __name__ == "__main__":
    data = read_input("input.txt")
    count_answers(data)
