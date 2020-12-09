from itertools import combinations


def read_input(filename):
    data = []
    with open(filename) as f:
        for line in f.readlines():
            num = int(line.replace("\n", ""))
            data.append(num)
    return data


def make_sums(data, low, high):
    comb = combinations(data[low:high], 2)
    sums = [sum(item) for item in list(comb)]
    return sums


def check_numbers(data):
    window_size = 25
    for i in range(len(data)):
        if i + window_size >= len(data):
            print("Reached end of list")
            break
        number_to_check = data[i + window_size]
        if number_to_check not in make_sums(data, i, i + window_size):
            print(f"OH NO - Wrong number: {number_to_check}")
            break


if __name__ == "__main__":
    data = read_input("input.txt")
    check_numbers(data)
