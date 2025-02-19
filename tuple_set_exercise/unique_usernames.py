numbers = int(input())
set_of_names = set()

for _ in range(numbers):
    name = input()
    set_of_names.add(name)

for n in set_of_names:
    print(n)