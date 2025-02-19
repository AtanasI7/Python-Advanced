size = int(input())
money = 100
matrix = []
gambler_pos = []
condition = True

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
        if 'G' in substring:
            gambler_pos = [row, substring.index('G')]
        matrix.append(substring)


matrix[gambler_pos[0]][gambler_pos[1]] = '-'

comm = input()

while comm != 'end':
    r, c = gambler_pos[0] + directions[comm][0], gambler_pos[1] + directions[comm][1]

    if not (0 <= r < size and 0 <= c < size):
        print(f"Game over! You lost everything!")
        condition = False
        break

    if matrix[r][c] == '-':
        gambler_pos = [r, c]

    elif matrix[r][c] == 'W':
        gambler_pos = [r, c]
        money += 100

    elif matrix[r][c] == 'P':
        gambler_pos = [r, c]
        money -= 200

        if money <= 0:
            print(f"Game over! You lost everything!")
            condition = False
            break

    elif matrix[r][c] == 'J':
        money += 100000
        print(f"You win the Jackpot!")
        break

    matrix[r][c] = '-'

    comm = input()

if condition:
    matrix[r][c] = 'G'
    print(f"End of the game. Total amount: {money}$")
    [print(''.join(row)) for row in matrix]