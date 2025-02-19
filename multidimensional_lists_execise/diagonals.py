rows = int(input())

matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]

primary = [matrix[row][row] for row in range(rows)]
second = [matrix[row][rows - row - 1] for row in range(rows)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in second)}. Sum: {sum(second)}")