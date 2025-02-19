from collections import deque

people_in_game = deque(input().split(' '))
toss_number = int(input()) - 1

while len(people_in_game) > 1:
    people_in_game.rotate(-toss_number)
    eliminated = people_in_game.popleft()
    print(f"Removed {eliminated}")


print(f"Last is {people_in_game.popleft()}")