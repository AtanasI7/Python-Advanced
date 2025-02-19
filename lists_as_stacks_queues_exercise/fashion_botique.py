clothes = list(map(int, input().split(' ')))
rack_capacity = int(input())
racks_count = 0


while clothes:
    removed_item = clothes.pop()
    if removed_item <= rack_capacity:
        sum_clothes = removed_item
        while rack_capacity > sum_clothes:
            if sum_clothes + clothes[-1] <= rack_capacity:
                racks_count += 1
                clothes.pop()
            else:
                break
        # second_removed_item = clothes[-1]
    #     if second_removed_item + removed_item <= rack_capacity:
    #         racks_count += 1
    #         clothes.pop()
    #     else:
    #         racks_count += 1
    # else:
    #     racks_count += 1

print(racks_count)