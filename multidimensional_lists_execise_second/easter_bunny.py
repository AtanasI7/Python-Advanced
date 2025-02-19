size = int(input())
matrix = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

bunny_pos = []
total_eggs = float('-inf')
best_path = []
best_direction = None

# matrix = [[int(i) if i.isdigit() else i for i in input().split()] for _ in range(size)]

for row in range(size):
    sub_string = []
    for i in input().split():
        if i.isdigit():
            sub_string.append(i)
        else:
            sub_string.append(i)

        if i == 'B':
            bunny_pos = [row, sub_string.index("B")]

    matrix.append(sub_string)

for dire in directions:
    cur_eggs = 0
    path = []

    r, c = [bunny_pos[0] + directions[dire][0],
            bunny_pos[1] + directions[dire][1]]

    while 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == 'X':
            break
        cur_eggs += int(matrix[r][c])
        path.append([r, c])

        r += directions[dire][0]
        c += directions[dire][1]

    if cur_eggs >= total_eggs:
        total_eggs = cur_eggs
        best_direction = dire
        best_path = path

print(best_direction)
[print(i) for i in best_path]
print(total_eggs)

























# for direction, positions in directions.items():
#     current_eggs = 0
#     r, c = positions[0], positions[1]
#     curr_row, curr_col = bunny_pos[0] + r, bunny_pos[1] + c
#
#     # while matrix[curr_row][curr_col] != 'X':
#     #     pass
#
#     while 0 <= curr_row < size and 0 <= curr_col < size and matrix[curr_row][curr_col] != 'X':
#         # curr_row, curr_col = bunny_pos[0] + r, bunny_pos[1] + c
#         current_eggs += int(matrix[curr_row][curr_col])
#         bunny_pos = curr_row, curr_col
#
#     if current_eggs > total_eggs:
#         total_eggs = current_eggs
#
# print(total_eggs)
