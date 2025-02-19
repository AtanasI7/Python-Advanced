from functools import reduce


def operate(command, *args):
    return reduce(lambda a, b: eval(f"{a}{command}{b}"), args)

    # if command == '+':
    #     return reduce(lambda a, b: a + b, args)
    # if command == '-':
    #     return reduce(lambda a, b: a - b, args)
    # if command == '*':
    #     return reduce(lambda a, b: a * b, args)
    # if command == '/':
    #     return reduce(lambda a, b: a / b, args)


print(operate("+", 1, 2, 3))