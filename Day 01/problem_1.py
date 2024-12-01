def calculate_total_distance(left, right):

    distance_list = []

    while len(left) > 0:
        minimum_val_left = min(left)
        minimum_val_right = min(right)

        distance_list.append(abs(minimum_val_left-minimum_val_right))

        left.remove(minimum_val_left)
        right.remove(minimum_val_right)

    return sum(distance_list)


filename = "test_case_1"

left = []
right = []

with open(filename, "r") as file:
    for line in file:
        if line.strip():  # Skip empty lines
            l, r = map(int, line.split())  # Split the line into two integers
            left.append(l)
            right.append(r)

result = calculate_total_distance(left, right)
print(result)
