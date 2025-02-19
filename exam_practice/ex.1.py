from collections import deque

worms = [int(x) for x in input().split()]
worms_copy = worms.copy()
holes = deque([int(x) for x in input().split()])
counter = 0

while worms and holes:
    cur_worm = worms.pop()
    cur_hole = holes.popleft()

    if cur_worm <= 0:
        holes.appendleft(cur_hole)
        continue

    elif cur_worm == cur_hole:
        counter += 1
        continue

    if cur_worm != cur_hole:
        cur_worm -= 3
        worms.append(cur_worm)

if counter > 0:
    print(f"Matches: {counter}")
else:
    print(f"There are no matches.")

if counter == len(worms_copy):
    print(f"Every worm found a suitable hole!")
elif not worms and counter > 0:
    print(f"Worms left: none")
else:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if holes:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")
else:
    print(f"Holes left: none")