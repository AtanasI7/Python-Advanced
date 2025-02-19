parentheses = input()
opening = ['(', '[', '{']
closing = [')', ']', '}']
stack = []
# ({}]

for i in parentheses:
    if i in opening:
        stack.append(i)
    elif i in closing:
        pos = closing.index(i)
        if len(stack) > 0:
            if opening[pos] == stack[len(stack) - 1]:
                stack.pop()
            else:
                a = 5

if len(stack) == 0:
    print('YES')
else:
    print('NO')