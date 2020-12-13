input_str = """1000053
19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,523,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,23,x,x,x,x,x,29,x,547,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"""

example_str = """939
7,13,x,x,59,x,31,19"""


def calc_first_future_bus(timestamp, bus):
    last_bus = timestamp - (timestamp % bus)

    return last_bus + bus


if __name__ == "__main__":
    timestamp, buses = input_str.split("\n")
    timestamp = int(timestamp)
    buses = [int(i) for i in buses.split(",") if i != "x"]
    print(timestamp, buses)

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

