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
            return number_to_check


def find_first_biggest_number(data, number):
    for idx, i in enumerate(data):
        if i >= number:
            return idx - 1


def find_contiguous_numbers_that_sum(data, number):
    high = 1
    idx_to_stop_at = find_first_biggest_number(data, number)
    for low in range(0, idx_to_stop_at + 1):
        high = 1
        while high <= idx_to_stop_at:
            if sum(data[low:high]) == number:
                numbers = sorted(data[low:high])
                print(f"smallest: {numbers[0]}")
                print(f"largest: {numbers[-1]}")
                print(f"sum: {numbers[0] + numbers[-1]}")
                return numbers[0] + numbers[-1]
            elif sum(data[low:high]) != number:
                high += 1


if __name__ == "__main__":
    data = read_input("input.txt")
    number = check_numbers(data)
    find_contiguous_numbers_that_sum(data, number)
