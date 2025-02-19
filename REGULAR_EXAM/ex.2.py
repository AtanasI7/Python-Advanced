size = int(input())
matrix = []
jetfighter_pos = []
armor_value = 300
enemy_planes = 4

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    substring = []

    for el in input().split():
        for e in el:
            substring.append(e)

        if 'J' in substring:
            jetfighter_pos = [row, substring.index('J')]
            substring[jetfighter_pos[1]] = '-'

    matrix.append(substring)

while armor_value > 0 and enemy_planes != 0:
    command = input()
    next_row, next_col = jetfighter_pos[0] + directions[command][0], jetfighter_pos[1] + directions[command][1]

    if matrix[next_row][next_col] == '-':
        jetfighter_pos = [next_row, next_col]

    elif matrix[next_row][next_col] == 'E':
        enemy_planes -= 1
        matrix[next_row][next_col] = '-'
        jetfighter_pos = [next_row, next_col]

        if enemy_planes == 0:
            matrix[next_row][next_col] = 'J'
            print(f"Mission accomplished, you neutralized the aerial threat!")
            break

        armor_value -= 100

        if armor_value == 0:
            matrix[next_row][next_col] = 'J'
            print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
            break

    elif matrix[next_row][next_col] == 'R':
        armor_value = 300
        matrix[next_row][next_col] = '-'
        jetfighter_pos = [next_row, next_col]

[print(''.join(row)) for row in matrix]



