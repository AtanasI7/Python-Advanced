numbers = input().split(',')
rows = int(numbers[0])
cols = int(numbers[1])

matrix = []
mouse_pos = []
cheese = 0


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(rows):
    substring = []
    for el in input().split():
        for e in el:
            substring.append(e)
        if 'M' in substring:
            mouse_pos = [row, substring.index('M')]
    cheese += substring.count('C')
    matrix.append(substring)

matrix[mouse_pos[0]][mouse_pos[1]] = '*'
current_cheese = 0


while True:
    command = input()

    if command == 'danger':
        if current_cheese < cheese:
            print(f"Mouse will come back later!")
            break

    r, c = mouse_pos[0] + directions[command][0], mouse_pos[1] + directions[command][1]

    if 0 <= r < rows and 0 <= c < cols:
        if matrix[r][c] == 'C':
            matrix[r][c] = '*'
            current_cheese += 1

            if current_cheese == cheese:
                matrix[r][c] = 'M'
                print(f"Happy mouse! All the cheese is eaten, good night!")
                break

        elif matrix[r][c] == 'T':
            matrix[r][c] = 'M'
            print(f"Mouse is trapped!")
            break

        elif matrix[r][c] == '@':
            continue

        mouse_pos = r, c

    else:
        print(f"No more cheese for tonight!")
        matrix[mouse_pos[0]][mouse_pos[1]] = 'M'
        break

[print(''.join(row)) for row in matrix]