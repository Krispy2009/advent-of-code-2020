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
    while True:
        (op, arg, idx) = data[curr_register]
        if idx in visited_ops:
            print(f"Duplicate instruction detected! Accumulator: {accumulator}")
            break
        visited_ops.append(idx)

        if op == "nop":
            curr_register += 1
        elif op == "acc":
            accumulator += arg
            curr_register += 1
        elif op == "jmp":
            curr_register += arg


if __name__ == "__main__":
    data = read_input("input.txt")
    run_program(data)
