def shoot(direction):
    r, c = shooter_pos[0] + directions[direction][0], shooter_pos[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if matrix[r][c] == 'x':
            matrix[r][c] = '.'
            return [r, c]


        r += directions[direction][0]
        c += directions[direction][1]


def move(direction, step):
    r = shooter_pos[0] + directions[direction][0] * step
    c = shooter_pos[1] + directions[direction][1] * step

    if not(0 <= r < SIZE and 0 <= c < SIZE):
        return shooter_pos
    if matrix[r][c] == 'x':
        return shooter_pos

    return [r, c]



SIZE = 5
matrix = []
shooter_pos = []
shooted_target_pos = []
all_targets = 0
hit_targets = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


for row in range(SIZE):
    matrix.append(input().split())

    if 'A' in matrix[row]:
        shooter_pos = [row, matrix[row].index('A')]

    all_targets += matrix[row].count('x')

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'move':
        shooter_pos = move(command[1], int(command[2]))

    elif command[0] == 'shoot':
        target_down_pos = shoot(command[1])

        if target_down_pos:
            shooted_target_pos.append(target_down_pos)
            hit_targets += 1

        if hit_targets == all_targets:
            print(f"Training completed! All {all_targets} targets hit.")
            break

if hit_targets < all_targets:
    print(f"Training not completed! {all_targets - hit_targets} targets left.")

[print(x) for x in shooted_target_pos]