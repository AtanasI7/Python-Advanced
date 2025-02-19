from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = [int(x) for x in input().split(', ')]

boxes = 0

while eggs and papers:
    curr_egg = eggs[0]
    curr_paper = papers[-1]

    if curr_egg == 13:
        eggs.popleft()

        papers[0], papers[-1] = papers[-1], papers[0]

        continue

    if curr_egg <= 0:
        eggs.popleft()
        continue

    if curr_paper + curr_egg <= 50:
        eggs.popleft()
        papers.pop()
        boxes += 1

    else:
        eggs.popleft()
        papers.pop()

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join([str(x) for x in eggs])}")

if papers:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers])}")