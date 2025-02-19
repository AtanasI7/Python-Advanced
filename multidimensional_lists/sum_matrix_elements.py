rows, col = [int(x) for x in input().split(',')]
total_amount = 0
matrix = []

for _ in range(rows):
    numbers = [int(x) for x in input().split(',')]
    total_amount += sum(numbers)
    matrix.append(numbers)

print(total_amount)
print(matrix)