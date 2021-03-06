example_str = """939
7,13,x,x,59,x,31,19"""

example_str = """939
17,x,13,19"""

example_str = """939
67,7,59,61"""

example_str = """939
67,x,7,59,61"""

example_str = """939
67,7,x,59,61"""

example_str = """939
1789,37,47,1889"""

input_str = """1000053
19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,547,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"""


def calc_first_future_bus(timestamp, bus):
    last_bus = timestamp - (timestamp % bus)

    return last_bus + bus


def part_1(timestamp, buses):
    closest_bus = None
    time_diff = None

    for bus in buses:
        first_bus = calc_first_future_bus(timestamp, bus)
        print(f"Bus {bus}: {first_bus}")
        this_time_diff = first_bus - timestamp
        if time_diff is None or time_diff > this_time_diff:
            time_diff = this_time_diff
            closest_bus = bus
    print(f"Closest bus: {closest_bus} - time diff: {time_diff}")
    print(f"Answer: {closest_bus * time_diff}")


def part_2(buses_list):
    buses = {k: v for v, k in enumerate(buses_list)}
    if "x" in buses:
        del buses["x"]
    last_bus = buses_list[-1]
    buses_list = [i for i in buses_list if i != "x"]
    multiplier = 1
    timestamp = 100_000_000_000_000
    while buses_list:
        for bus in buses_list[:]:
            if ((timestamp) + buses[bus]) % bus != 0:
                timestamp += multiplier
                break
            else:
                buses_list.remove(bus)
                multiplier *= bus

            if bus == last_bus:
                print(timestamp)
                return timestamp


if __name__ == "__main__":
    timestamp, buses = input_str.split("\n")
    timestamp = int(timestamp)
    all_buses = [int(i) if i != "x" else i for i in buses.split(",")]
    buses = [int(i) for i in buses.split(",") if i != "x"]

    part_1(timestamp, buses)
    part_2(all_buses)
