number = int(input())
parking_lot = set()


for _ in range(number):
    command, car_number = input().split(', ')
    if command == 'IN':
        parking_lot.add(car_number)
    elif command == 'OUT':
        parking_lot.remove(car_number)

if parking_lot:
    [print(car) for car in parking_lot]
    # for car in parking_lot:
    #     print(car)
else:
    print('Parking Lot is Empty')