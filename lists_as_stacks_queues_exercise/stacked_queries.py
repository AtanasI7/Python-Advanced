number = int(input())
command = input().split(' ')
stack = list()

for i in range(number):
    if len(command) > 1:
        _, current_num = command
        stack.append(current_num)

    else:
        command = int(command[0])
        if command == 2:
            if len(stack) > 1:
                stack.pop()

        elif command == 3:
            print(max(stack))

        elif command == 4:
            print(min(stack))


    command = input().split(' ')

print(', '.join(stack[::-1]))



