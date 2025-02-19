from collections import deque

people = deque()
name = input()

while name != 'End':

    if name == 'Paid':
        while people:
            print(people.popleft())

    else:
        people.append(name)
    name = input()

print(f"{len(people)} people remaining.")