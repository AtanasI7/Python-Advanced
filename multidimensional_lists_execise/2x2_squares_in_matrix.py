rows, cols = [int(el) for el in input().split(' ')]

counter = 0

matrix = [input().split() for i in range(rows)]

for row in range(rows - 1):
    for col in range(cols - 1):
        current_el = matrix[row][col]
        next_el = matrix[row][col + 1]
        under_el = matrix[row + 1][col]
        diagonal_el = matrix[row + 1][col + 1]

        if current_el == next_el and current_el == under_el and current_el == diagonal_el:
            counter += 1

print(counter)