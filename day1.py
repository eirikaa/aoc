def list_data(input_data):
    with open(input_data, "r+") as f:
        data = [int(data.strip()) for data in f]
    return data


def compute_change(data):
    change = {"decrease": 0, "increase":0, "no_change":0}
    for n, record in enumerate(data):
        if n:
            if record < prev_record:
                change["decrease"] += 1
            elif record > prev_record:
                change["increase"] += 1
            else:
                change["no_change"] += 1
        prev_record = record
    return change

def print_solution(change):
    print(f"Number of increase: {change['increase']}")

if __name__ == "__main__":
    input_data = "day1_input.txt"
    data = list_data(input_data)
    change = compute_change(data)
    print_solution(change)