def calculate_similarity_score(left, right):
    score_list = []

    for i in left:
        count = 0
        for j in right:
            if i == j:
                count += 1
        score_list.append((i * count))

    return sum(score_list)


filename = "test_case"

left = []
right = []

with open(filename, "r") as file:
    for line in file:
        if line.strip():  # Skip empty lines
            l, r = map(int, line.split())  # Split the line into two integers
            left.append(l)
            right.append(r)

result = calculate_similarity_score(left, right)
print(result)
