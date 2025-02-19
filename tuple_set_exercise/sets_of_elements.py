len_sets = [int(x) for x in input().split()]
first, second = len_sets

first_set = set()
second_set = set()

for _ in range(first):
    current_n = input()
    first_set.add(current_n)

for _ in range(second):
    current_m = input()
    second_set.add(current_m)

intersection = first_set & second_set

for i in intersection:
    print(i)
