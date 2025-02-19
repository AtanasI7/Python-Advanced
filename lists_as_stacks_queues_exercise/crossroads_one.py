from collections import deque

green_light_duration = int(input())
free_window = int(input())
data = deque()
counter_passed_cars = 0

while True:
    car = input()

    if car == 'END':
        break

    elif car == 'green':
        green_light_duration_copy = green_light_duration

        while data:
            passed_car = data.popleft()

            if green_light_duration_copy > 0:
                green_light_duration_copy -= len(passed_car)
                counter_passed_cars += 1
                if green_light_duration_copy < 0:
                    if green_light_duration_copy + free_window >= len(passed_car) - green_light_duration_copy:
                        counter_passed_cars += 1
            else:
                condition = True
                # if len(data) > 0:
                #     if green_light_duration_copy:
                #         green_light_duration_copy -= len(data.popleft())
                #         a = 5

    else:
        data.append(car)

