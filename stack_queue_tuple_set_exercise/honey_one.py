from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_nectar = 0

functions = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else 0,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
    else:
        total_nectar += abs(functions[symbols.popleft()](current_bee, current_nectar))

print(f"Total honey made: {total_nectar}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")

if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
