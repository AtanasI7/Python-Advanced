presents = int(input())
size = int(input())

matrix = []
santa_pos = []
nice_kids_counter = 0


directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1),
}

for row in range(size):
    line = input().split()

    if 'S' in line:
        santa_pos = row, line.index('S')
        line[santa_pos[1]] = '-'
    matrix.append(line)

command = input()

while command != 'Christmas morning' and presents > 0:
    next_row, next_col = santa_pos[0] + directions[command][0], santa_pos[1] + directions[command][1]

    if 0 <= next_row < size and 0 <= next_col < size:
        if matrix[next_row][next_col] == 'V':
            matrix[next_row][next_col] = '-'
            nice_kids_counter += 1
            presents -= 1

        elif matrix[next_row][next_col] == 'X':
            matrix[next_row][next_col] = '-'

        elif matrix[next_row][next_col] == 'C':
            matrix[next_row][next_col] = '-'

            if matrix[next_row - 1][next_col] in ['X', 'V']:
                matrix[next_row - 1][next_col] = '-'
                presents -= 1

            if matrix[next_row][next_col - 1] in ['X', 'V']:
                matrix[next_row][next_col - 1] = '-'
                presents -= 1

            if matrix[next_row + 1][next_col] in ['X', 'V']:
                matrix[next_row + 1][next_col] = '-'
                presents -= 1

            if matrix[next_row][next_col + 1] in ['X', 'V']:
                matrix[next_row][next_col + 1] = '-'
                presents -= 1

    santa_pos = next_row, next_col

    command = input()
print(matrix)