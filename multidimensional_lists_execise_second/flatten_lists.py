data = input().split('|')

sub_list = []

for item in data[::-1]:
    sub_list.extend(item.split())

print(*sub_list)
