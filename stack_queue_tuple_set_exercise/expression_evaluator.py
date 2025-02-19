data = input().split(' ')
calculations = []
result = 1

for el in data:
    if el.isdigit():
        calculations.append(int(el))

    if len(calculations) >= 2:

        if el == '*':
            for num in calculations:
                result *= num
            calculations.clear()
            calculations.append(result)

        elif el == '+':
            for num in calculations:
                result += num
            calculations.clear()
            calculations.append(result)

        elif el == '-':
            for num in calculations:
                result -= num
            calculations.clear()
            calculations.append(result)

        elif el == '/':
            for num in calculations:
                result /= num
            calculations.clear()
            calculations.append(result)


print(*calculations)