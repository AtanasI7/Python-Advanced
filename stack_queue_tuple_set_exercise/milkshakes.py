from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:
    curr_choco = chocolates.pop()
    curr_cup_milk = cups_of_milk.popleft()

    if curr_choco == curr_cup_milk:
        milkshakes += 1

    else:
        cups_of_milk.appendleft(curr_cup_milk)
        cups_of_milk.rotate(-1)
        chocolates.append(curr_choco - 5)

if milkshakes >= 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print(f"Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print(f"Milk: empty")