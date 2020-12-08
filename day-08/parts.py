def read_input(filename):
    data = []
    with open(filename) as f:
        for idx, line in enumerate(f.readlines()):
            op, arg = line.replace("\n", "").split(" ")
            data.append((op, int(arg), idx))
    return data


def run_program(data):
    accumulator = 0
    visited_ops = []
    curr_register = 0
    try:
        while True:
            (op, arg, idx) = data[curr_register]
            if idx in visited_ops:
                print(f"Duplicate instruction detected! Accumulator: {accumulator}")
                return -1
            visited_ops.append(idx)
            if op == "nop":
                curr_register += 1
            elif op == "acc":
                accumulator += arg
                curr_register += 1
            elif op == "jmp":
                curr_register += arg
    except IndexError:
        print(f"TERMINATED wohoo! {accumulator}")
        return 0


def try_fixing_ops(data):
    for (op, arg, idx) in data:
        new_data = data[:]
        if op == "nop":
            new_data[idx] = ("jmp", arg, idx)
        elif op == "jmp":
            new_data[idx] = ("nop", arg, idx)
        res = run_program(new_data)
        if not res:
            break


if __name__ == "__main__":
    data = read_input("input.txt")
    try_fixing_ops(data)
