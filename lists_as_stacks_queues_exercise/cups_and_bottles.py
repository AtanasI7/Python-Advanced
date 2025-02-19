from collections import deque

cups_capacity = deque(input().split(' '))
bottles_capacity = input().split(' ')
wasted_water = 0

while True:
    current_cup = int(cups_capacity.popleft())
    current_bottle = int(bottles_capacity.pop())

    if current_bottle > current_cup:
        wasted_water += current_bottle - current_cup
    elif current_cup > current_bottle:
        while current_cup > 0:
            current_cup -= current_bottle
            if current_cup < 0:
                wasted_water -= current_cup
                break
            if current_cup == 0:
                break
            current_bottle = int(bottles_capacity.pop())

    if not cups_capacity:
        print(f"Bottles: {' '.join(bottles_capacity)}")
        print(f"Wasted liters of water: {wasted_water}")
        break

    if not bottles_capacity:
        print(f"Cups: {' '.join(cups_capacity)}")
        print(f"Wasted litters of water: {wasted_water}")
        break




