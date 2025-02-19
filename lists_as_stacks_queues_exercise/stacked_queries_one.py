number = int(input())
query = input()
stack = list()

for i in range(number):
    if len(query) == 1:
        query = int(query)
        if query == 2:
            if stack:
                stack.pop()
        elif query == 3:
            if stack:
                print(max(stack))
        elif query == 4:
            if stack:
                print(min(stack))

    else:
        query = query.split(' ')
        _, current_num = query
        stack.append(current_num)

    query = input()


result = ', '.join(stack[::-1])
print(result)
