def list_data(input_data):
    with open(input_data, "r+") as f:
        data = [int(data.strip()) for data in f]
    return data


def compute_change(data):
    change = {"decrease": 0, "increase": 0, "no_change": 0}
    for i, record in enumerate(data):
        if i:
            if record < prev_record:
                change["decrease"] += 1
            elif record > prev_record:
                change["increase"] += 1
            else:
                change["no_change"] += 1
        prev_record = record
    return change


def compute_change_part_two(data):
    change = {"decrease": 0, "increase": 0, "no_change": 0}
    for i in range(len(data) - 3):
        if sum(data[i : i + 3]) < sum(data[i + 1 : i + 4]):
            change["increase"] += 1
    return change


def print_solution(change):
    print(f"Number of increase: {change['increase']}")


if __name__ == "__main__":
    input_data = "day1_input.txt"
    data = list_data(input_data)
    change = compute_change(data)
    change_part_two = compute_change_part_two(data)
    print("PART 1")
    print_solution(change)
    print("PART 2")
    print_solution(change_part_two)
