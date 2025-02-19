rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

max_result = float('-inf')
sub_matrix = []

for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        under_element = matrix[row_index + 1][col_index]
        diagonal_element = matrix[row_index + 1][col_index + 1]

        current_result = current_element + next_element + under_element + diagonal_element

        if current_result > max_result:
            max_result = current_result
            sub_matrix = [[current_element, next_element], [under_element, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_result)