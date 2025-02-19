parentheses = input()
opening = ['(', '[', '{']
closing = [')', ']', '}']
stack = list()

for par in parentheses:
    if par in opening:
        stack.append(par)
    elif par in closing:
        position = closing.index(par)
        if opening[position] == stack[len(stack) - 1]:
            stack.pop()


if len(stack) == 0:
    print('YES')
else:
    print('NO')


