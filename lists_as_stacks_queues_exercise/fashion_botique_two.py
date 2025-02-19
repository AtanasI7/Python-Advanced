clothes = [int(x) for x in input().split(' ')]
capacity = int(input())
rack_space = 1
current_capacity = capacity

while clothes:
    cloth = clothes.pop()

    if current_capacity >= cloth:
        current_capacity -= cloth
    else:
        rack_space += 1
        current_capacity = capacity - cloth


print(rack_space)