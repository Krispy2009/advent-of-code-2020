from validation import validate_date, validate_ecl, validate_hcl, validate_hgt, validate_pid


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
            prepped_line = f"{prepped_line} {line}"
    return prepped_data


def validate_data(data):
    valid_args = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_count = 0
    valid_and_complete_count = 0
    for line in data:
        line_valid_count = 0
        for arg in valid_args:
            if arg not in line:
                print(f"{arg} not in {line}")
            else:
                line_valid_count += 1
        if line_valid_count == len(valid_args):
            valid_count += 1
            params = make_dict_from_line(line)
            validation_results = [
                validate_date(params["byr"], 1920, 2002),
                validate_date(params["iyr"], 2010, 2020),
                validate_date(params["eyr"], 2020, 2030),
                validate_hgt(params["hgt"]),
                validate_hcl(params["hcl"]),
                validate_ecl(params["ecl"]),
                validate_pid(params["pid"]),
            ]
            if sum(validation_results) == len(valid_args):
                valid_and_complete_count += 1
    print(f"Valid passports: {valid_count}")
    print(f"Valid and complete passports: {valid_and_complete_count}")


def make_dict_from_line(line):
    parsed_dict = {}
    parts = line.split(" ")
    parts = [p for p in parts if p != ""]
    for part in parts:
        (key, value) = part.split(":")
        parsed_dict[key] = value
    return parsed_dict


if __name__ == "__main__":
    data = read_input("input.txt")
    data = prep_input(data)
    validate_data(data)
