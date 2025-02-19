from collections import deque

rows, cols = [int(x) for x in input().split()]
word = list(input())
word_copy = deque(word)



for row in range(rows):
    sub_string = []
    while cols > len(word_copy):
        word_copy.extend(word)

    if row % 2 == 0:
        for i in range(cols):
            sub_string.append(word_copy.popleft())
        print(*sub_string, sep='', end='')
    else:
        for i in range(cols):
                sub_string.append(word_copy.popleft())
        print(*sub_string[::-1], sep='', end='')
    print()


    # if row % 2 == 0:
    #     print(*[word_copy.popleft() for _ in range(cols)], sep='')
    # else:
    #     print(*[word_copy.popleft() for _ in range(cols)][::-1], sep='')