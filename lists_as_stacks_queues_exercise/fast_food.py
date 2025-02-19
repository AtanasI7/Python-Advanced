from collections import deque

food_quantity = int(input())
people_waiting = deque([int(x) for x in input().split(' ')])
print(max(people_waiting))

for i in people_waiting.copy():
    if food_quantity >= i:
        people_waiting.popleft()
        food_quantity -= i
    else:
        break

if people_waiting:
    print(f"Orders left:", *people_waiting)
else:
    print('Orders complete')


