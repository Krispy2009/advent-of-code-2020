import re
import itertools

mem_re = re.compile(r"mem\[(?P<address>\d+)\] = (?P<value>\d+)")


def process_program(mask, memory, instructions):
    for instruction in instructions:
        value = list(f"{bin(instruction[1])[2:]:0>36}")
        for idx, bit in enumerate(mask):
            if bit != "X":
                value[idx] = bit

        memory[instruction[0]] = int("".join(value), 2)
    return memory


def process_program_v2(mask, memory, instructions):
    for instruction in instructions:
        address = list(f"{bin(instruction[0])[2:]:0>36}")
        idx_to_change = []
        for idx, bit in enumerate(mask):
            if bit == "0":
                continue
            elif bit == "1":
                address[idx] = bit
            elif bit == "X":
                idx_to_change.append(idx)

        floating_bits = len(idx_to_change)
        perms = [x for x in itertools.product("01", repeat=floating_bits) if floating_bits > 0]
        for perm in perms:
            new_address = address[:]
            for perm_idx, i in enumerate(idx_to_change):
                new_address[i] = perm[perm_idx]
            # print(
            #     f'Writing {instruction[1]} to memory address {"".join(new_address)} (decimal {int("".join(new_address), 2)})'
            # )
            memory[int("".join(new_address), 2)] = instruction[1]
    return memory


if __name__ == "__main__":
    mask = None
    memory = {}
    instructions = []

    with open("input.txt") as f:
        for line in f.readlines():
            if line.startswith("mask") and not len(instructions):
                mask = line.split(" = ")[1].replace("\n", "")
            elif line.startswith("mem"):
                address, value = re.match(mem_re, line).groups()
                instructions.append((int(address), int(value)))
            else:
                # Process program
                # memory = process_program(mask, memory, instructions)
                memory = process_program_v2(mask, memory, instructions)
                if line.startswith("mask"):
                    instructions = []
                    mask = line.split(" = ")[1].replace("\n", "")

        print(f"Ans: {sum(memory.values())}")
