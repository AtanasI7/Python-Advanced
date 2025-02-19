size = int(input())
matrix = []

alice_pos = []
needed_bags_tea = 0
condition = False

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),

}

for row in range(size):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        alice_pos = [row, matrix[row].index('A')]
        matrix[alice_pos[0]][alice_pos[1]] = '*'

while needed_bags_tea < 10:

    command = input()
    if command in directions.keys():
        cur_row, cur_col = [
            alice_pos[0] + directions[command][0],
            alice_pos[1] + directions[command][1],
        ]

    if not (0 <= cur_row < size and 0 <= cur_col < size):
        print("Alice didn't make it to the tea party.")
        [print(*row) for row in matrix]
        break

    current_position = matrix[cur_row][cur_col]

    if current_position.isdigit():
        needed_bags_tea += int(current_position)

    if current_position == 'R':
        matrix[cur_row][cur_col] = '*'
        print("Alice didn't make it to the tea party.")
        [print(*row) for row in matrix]
        break

    matrix[cur_row][cur_col] = '*'
    alice_pos[0] = cur_row
    alice_pos[1] = cur_col

if needed_bags_tea >= 10:
    print(f"She did it! She went to the party.")
    [print(*i) for i in matrix]







