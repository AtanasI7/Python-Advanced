from collections import deque


names = deque(input().split(', '))

SIZE = 6
matrix = []
condition = False
counter = 0

for row in range(SIZE):
    matrix.append(input().split())

while True:
    position = input()
    row = int(position[1])
    col = int(position[4])

    if matrix[row][col] == 'E':
        print(f"{names[0]} found the exit and wins the game!")
        break

    elif matrix[row][col] == "T":
        print(f"{names[0]} is out of the game! The winner is {names[1]}.")
        break

    elif matrix[row][col] == 'W':
        condition = True
        names.append(names.popleft())
        print(f"{names[0]} hits a wall and needs to rest.")

    if condition:
        counter += 1

        if counter == 3:
            counter = 0
            condition = False
        continue

    if not condition:
        names.append(names.popleft())

