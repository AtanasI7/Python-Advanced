num = int(input())

matrix = []

for _ in range(num):
    matrix.append(list(input()))

searched_element = input()
condition = False

for row_index in range(num):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_element:
            print(f"({row_index}, {col_index})")
            condition = True
            break

    if condition:
        break

if not condition:
    print(f"{searched_element} does not occur in the matrix")
