from collections import deque


def fill_the_box(height, length, width, *args):
    capacity = height * length * width
    cubes = deque(args)

    while cubes[0] != 'Finish':
        capacity -= cubes.popleft()

        if capacity < 0:
            space_more_needed = sum(n for n in cubes if n != 'Finish')
            return f"No more free space! You have {space_more_needed + abs(capacity)} more cubes."

    return f"There is free space in the box. You could put {capacity} more cubes."


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
