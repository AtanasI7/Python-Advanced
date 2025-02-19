rows_cols = int(input())
matrix = [[int(x) for x in input().split(' ')] for n in range(rows_cols)]
coordinates = ((int(x) for x in c.split(',')) for c in input().split())

directions = (
    (-1, 0),    # up
    (-1, 1),    # up-right
    (0, 1),     # right
    (1, 1),     # down-right
    (1, 0),     # down
    (1, -1),    # down-left
    (0, -1),    # left
    (-1, -1),   # up-left
    (0, 0)      # current
)

for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue

    for x, y in directions:
        r, c = row + x, col + y

        if 0 <= r < rows_cols and 0 <= c <= rows_cols:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0

live_cells = []
for row in range(rows_cols):
    for num in matrix[row]:
        if num > 0:
            live_cells.append(num)

print(f"Alive cells: {len(live_cells)}")
print(f"Sum: {sum(live_cells)}")
for row in matrix:
    print(*row)