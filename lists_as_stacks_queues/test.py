from collections import deque

a = deque([3, 10, 5, 6])

deleted = a.popleft()

print(deleted)