first_name, second_name = input().split(', ')

SIZE = 6
matrix = []
condition = False

for row in range(SIZE):
    matrix.append(input().split())

while True:
    position = input()
    row = int(position[1])
    col = int(position[4])

    if matrix[row][col] == 'E':
        print(f"{first_name} found the exit and wins the game!")
        break

    elif matrix[row][col] == "T":
        print(f"{first_name} is out of the game! The winner is {second_name}.")
        break

    elif matrix[row][col] == 'W':
        condition = True
        print(f"{first_name} hits a wall and needs to rest.")

    if condition:
        pass

    first_name, second_name = second_name, first_name

