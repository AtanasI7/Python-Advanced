numbers = input().split(' ')
for i in range(len(numbers)):
    last_num = numbers.pop()
    print(last_num, end=' ')