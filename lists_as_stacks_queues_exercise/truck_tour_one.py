from collections import deque

pump_data = deque([[int(x) for x in input().split(' ')] for i in range(int(input()))])

pump_data_copy = pump_data.copy()
gas_tank = 0
count = 0

while pump_data_copy:
    petrol, distance = pump_data_copy.popleft()

    gas_tank += petrol

    if gas_tank >= distance:
        gas_tank -= distance
    else:
        pump_data.rotate(-1)
        pump_data_copy = pump_data
        gas_tank = 0
        count += 1

print(count)