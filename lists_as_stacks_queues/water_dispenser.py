from collections import deque

water = int(input())
name = input()
people = deque()

while name != 'Start':
    people.append(name)
    name = input()

data = input()

while data != 'End':
    data = data.split(' ')

    if len(data) > 1:
        _, refilled_water = data
        water += int(refilled_water)

    else:
        data = int(data[0])
        if data <= water:
            removed_person = people.popleft()
            water -= data
            print(f"{removed_person} got water")

        else:
            print(f"{people.popleft()} must wait")

    data = input()


print(f"{water} liters left")

