rows = int(input())
flatten = []

for row in range(rows):
    data = [int(x) for x in input().split(', ')]
    flatten.extend(data)

print(flatten)

# flatten = []
#
# for row in matrix:
#     for el in row:
#         flatten.append(el)
#
# flatten = [el for row in matrix for el in row]
#
# print(flatten)