rows = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

# first = sum([matrix[row][row] for row in range(rows)])
# second = sum([matrix[row][rows - row - 1] for row in range(rows)])

first_sum, second_sum = 0, 0

for row in range(rows):
    first_sum += matrix[row][rows]
    second_sum += matrix[row][rows - row - 1]

print(abs(first_sum - second_sum))