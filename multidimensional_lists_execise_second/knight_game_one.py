size = int(input())
matrix = [list(input()) for _ in range(size)]

pos_numbers = [-2, -1, 1, 2]
positions = [(x, y) for x in pos_numbers for y in pos_numbers if abs(x) != abs(y)]

removed_knights = 0

for row in range(size):
    for col in range(size):
        pass