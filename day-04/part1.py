def read_input(file):

    data = []
    with open(file, "r") as f:
        for d in f.readlines():
            data.append(d.replace("\n", ""))

    data.append("")
    return data


def prep_input(data):
    prepped_data = []
    prepped_line = ""
    for line in data:
        if line == "":
            prepped_data.append(prepped_line)
            prepped_line = ""
        else:
            prepped_line = f"{prepped_line}{line}"
    print(len(prepped_data))
    return prepped_data


def validate_data(data):
    valid_args = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_count = 0
    for line in data:
        line_valid_count = 0
        for arg in valid_args:
            if arg not in line:
                print(f"{arg} not in {line}")
            else:
                line_valid_count += 1
        if line_valid_count == len(valid_args):
            valid_count += 1
    print(valid_count)


if __name__ == "__main__":
    data = read_input("input.txt")
    data = prep_input(data)
    validate_data(data)
