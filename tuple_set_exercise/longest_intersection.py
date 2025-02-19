lines_number = int(input())
beginning = set()
ending = set()

for _ in range(lines_number):
    current_beginning = set()
    current_ending = set()
    first, second = input().split('-')
    start = str(first).replace(',', ' ')
    end = str(second).replace(',', ' ')

    for i in range(int(start[0]), int(start[1]) + 1):
        current_beginning.add(i)

    for i in range(int(end[0]), int(end[1]) + 1):
        current_ending.add(i)

    if current_beginning & current_ending > beginning & ending:
        beginning, ending = current_beginning, current_ending

final_intersection = beginning & ending
print(final_intersection)
