def part_one(input_data):
    directions = {"depth": 0, "horizontal": 0}
    with open(input_data, "r+") as f:
        for data in f:
            command = data.split(" ")
            if "forward" in command[0]:
                directions["horizontal"] += int(command[1])
            elif "up" in command[0]:
                directions["depth"] -= int(command[1])
            elif "down" in command[0]:
                directions["depth"] += int(command[1])
    return directions


def part_two(input_data):
    directions = {"aim": 0, "horizontal": 0, "depth": 0}
    with open(input_data, "r+") as f:
        for data in f:
            command = data.split(" ")
            if "forward" in command[0]:
                directions["horizontal"] += int(command[1])
                directions["depth"] += int(command[1]) * directions["aim"]
            elif "up" in command[0]:
                directions["aim"] -= int(command[1])
            elif "down" in command[0]:
                directions["aim"] += int(command[1])

    return directions

def print_solution(directions):
    position = directions["depth"] * directions["horizontal"]
    print(f"Position: {position}")


if __name__ == "__main__":
    input_data = "day2_input.txt"
    directions = part_one(input_data)
    print_solution(directions)
    directions = part_two(input_data)
    print_solution(directions)