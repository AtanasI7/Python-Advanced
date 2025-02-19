from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
total_nectar = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()

        if current_symbol == '+':
            total_nectar += current_nectar + current_bee
        elif current_symbol == '-':
            total_nectar += abs(current_nectar - current_bee)
        elif current_symbol == '/':
            if current_nectar == 0:
                total_nectar += 0
            else:
                total_nectar += current_nectar / current_bee
        elif current_symbol == '*':
            total_nectar += current_nectar * current_bee

    else:
        bees.appendleft(current_bee)


print(f"Total honey made: {total_nectar}")

if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")

if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
