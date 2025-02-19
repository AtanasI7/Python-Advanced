size = int(input())
money = 100
matrix = []
gambler_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    data = input()

    if 'G' in data:
        gambler_pos = [row, data.index('G')]

    matrix.append(data.split())

comm = input()
# matrix[gambler_pos[0]][gambler_pos[1]] = '-'

while comm != 'end':
    r, c = gambler_pos[0] + directions[comm][0], gambler_pos[1] + directions[comm][1]

    if not (0 <= r < size and 0 <= c < size) or money <= 0:
        print(f"Game over! You lost everything!")
        break
    print(matrix[r][c])
    if matrix[r][c] == '-':
        gambler_pos = [r, c]
        continue

    elif matrix[r][c] == 'W':
        gambler_pos = [r, c]
        money += 100

    elif matrix[r][c] == 'P':
        gambler_pos = [r, c]
        money -= 200

    elif matrix[r][c] == 'J':
        money += 100000
        break

    matrix[r][c] = 'G'

    comm = input()

print(matrix)