def number_of_safe_reports(reports):

    safe_count = 0

    for report in reports:

        condition = False

        is_sorted_list = is_sorted(report)

        for level in range(len(report) - 1):

            lvl_differ = abs(report[level] - report[level+1])
            if (lvl_differ < 1 or lvl_differ > 3) or (not is_sorted_list):
                condition = True
        if not condition:
            safe_count += 1

    return safe_count


def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or \
           all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))


filename = "test_case"

rows = []

with open(filename, "r") as file:
    for line in file:
        if line.strip():
            row = list(map(int, line.split()))
            rows.append(row)

result = number_of_safe_reports(rows)
print(result)
