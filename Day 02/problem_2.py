def number_of_safe_reports(reports):
    def is_safe(report):

        return (all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or
                all(report[i] >= report[i + 1] for i in range(len(report) - 1))) and \
               all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))

    safe_count = 0

    for report in reports:

        if is_safe(report):
            safe_count += 1
            continue

        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                safe_count += 1
                break

    return safe_count


# Read the test case file
filename = "test_case"
rows = []

with open(filename, "r") as file:
    for line in file:
        if line.strip():
            row = list(map(int, line.split()))
            rows.append(row)

# Get the result
result = number_of_safe_reports(rows)
print(result)
