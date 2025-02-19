input_lines = int(input())
unique_elems = set()


for _ in range(input_lines):
    elements = input().split(' ')

    if len(elements) > 1:
        for el in elements:
            unique_elems.add(el)
    else:
        unique_elems.add(''.join(elements))

[print(x) for x in unique_elems]
