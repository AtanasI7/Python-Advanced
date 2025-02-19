expression = input()
paten_indexes = list()

for index in range(0, len(expression)):
    if expression[index] == '(':
        paten_indexes.append(index)
    elif expression[index] == ')':
        start_index = paten_indexes.pop()
        end_index = index + 1
        print(expression[start_index:end_index])