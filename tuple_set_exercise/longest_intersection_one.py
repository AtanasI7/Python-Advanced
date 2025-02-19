number = int(input())
starting = set()
ending = set()

for _ in range(number):
    data = input().split('-')
    start = [int(x) for x in data[0].split(',')]
    end = [int(x) for x in data[1].split(',')]
    current_starting = set()
    current_ending = set()

    [current_starting.add(n) for n in range(start[0], start[1] + 1)]
    # first_set = set(range(start[0], start[0] + 1))

    [current_ending.add(m) for m in range(end[0], end[1] + 1)]
    # second_set = set(range(end[0], end[0] + 1))

    if len(current_starting.intersection(current_ending)) > len(starting.intersection(ending)):
        starting = current_starting
        ending = current_ending

result = [str(x) for x in starting.intersection(ending)]
print(f"Longest intersection is [{', '.join(result)}] with length {len(result)}")