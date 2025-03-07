size = int(input())
matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

command = input().split()

while command[0] != 'END':
    type_command, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if not (0 <= row < size and 0 <= col < size):
        print('Invalid coordinates')
    elif type_command == 'Add':
        matrix[row][col] += value
    elif type_command == 'Subtract':
        matrix[row][col] -= value

    command = input().split()

[print(*i) for i in matrix]