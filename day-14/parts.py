import re

mem_re = re.compile(r"mem\[(?P<address>\d+)\] = (?P<value>\d+)")


def process_program(mask, memory, instructions):
    for instruction in instructions:
        value = list(f"{bin(instruction[1])[2:]:0>36}")
        for idx, bit in enumerate(mask):
            if bit != "X":
                value[idx] = bit

        memory[instruction[0]] = int("".join(value), 2)
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
                memory = process_program(mask, memory, instructions)
                if line.startswith("mask"):
                    instructions = []
                    mask = line.split(" = ")[1].replace("\n", "")

        print(f"Ans: {sum(memory.values())}")
