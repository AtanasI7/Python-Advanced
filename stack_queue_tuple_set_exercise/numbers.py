first = set([int(x) for x in input().split(' ')])
second = set([int(x) for x in input().split(' ')])
lines_number = int(input())

for _ in range(lines_number):
    first_command, second_command, *data = input().split(' ')
    command = first_command + " " + second_command

    if command == "Add First":
        [first.add(int(el)) for el in data]

    elif command == 'Add Second':
        [second.add(int(el)) for el in data]

    elif command == "Remove First":
        [first.discard(int(el)) for el in data]

    elif command == "Remove Second":
        [second.discard(int(el)) for el in data]

    elif command == "Check Subset":
        print(first.issubset(second) or second.issubset(first))


print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')