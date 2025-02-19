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
    condition = False

    for direction, position in directions.items():
        command = input()
        cur_row, cur_col = [
            alice_pos[0] + position[0],
            alice_pos[1] + position[1]
        ]
        current_position = matrix[cur_row][cur_col]

        if current_position == 'R':
            condition = True
            break

        if not (0 <= cur_row < size and 0 <= cur_col < size):
            condition = True
            break

        if command == direction:
            if current_position.isdigit():
                needed_bags_tea += current_position

            matrix[current_position] = '*'

    if condition:
        break


print(matrix)



