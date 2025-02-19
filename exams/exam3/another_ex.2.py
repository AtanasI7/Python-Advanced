rows, cols = [int(x) for x in input().split()]
matrix = []
biker_pos = []

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
        if 'B' in substring:
            biker_pos = [row, substring.index('B')]
        matrix.append(substring)

copy_biker_pos = biker_pos.copy()



while True:
    command = input()
    next_row, next_col = biker_pos[0] + directions[command][0], biker_pos[1] + directions[command][1]

    if 0 <= next_row < rows and 0 <= next_col < cols:
        if matrix[next_row][next_col] == 'P':
            matrix[next_row][next_col] = 'R'
            print(f"Pizza is collected. 10 minutes for delivery.")

        elif matrix[next_row][next_col] == '*':
            matrix[copy_biker_pos[0]][copy_biker_pos[1]] = ' '
            continue

        elif matrix[next_row][next_col] == 'A':
            matrix[next_row][next_col] = 'P'
            print(f"Pizza is delivered on time! Next order...")
            break

        elif matrix[next_row][next_col] == '-':
            matrix[next_row][next_col] = '.'

        biker_pos = next_row, next_col

    else:
        print(f"The delivery is late. Order is canceled.")
        break

[print(''.join(row)) for row in matrix]