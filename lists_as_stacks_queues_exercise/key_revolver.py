from collections import deque

price_per_bullet = int(input())
gun_barrel_size = int(input())
all_bullets = [int(i) for i in input().split(' ')]
locks = deque([int(x) for x in input().split(' ')])
intelligence = int(input())
locks_copy = locks.copy()
barrel_counter = 0
condition = False
second_condition = False

for lock in locks_copy:
    if second_condition:
        break

    while True:
        current_bullet = all_bullets.pop()
        intelligence -= price_per_bullet
        barrel_counter += 1
        if lock >= current_bullet:
            print(f"Bang!")
            locks.popleft()
            condition = True
        else:
            print('Ping!')

        if barrel_counter == gun_barrel_size:
            barrel_counter = 0
            if all_bullets:
                print("Reloading!")
            else:
                second_condition = True
                break

        if condition:
            condition = False
            break

if len(locks) == 0:
    print(f"{len(all_bullets)} bullets left. Earned ${intelligence}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")