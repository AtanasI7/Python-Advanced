import os

file_name = 'text.txt'
path = os.path.join('resources', file_name)

try:
    file = open(path)
    print(f"File found")
except FileNotFoundError:
    print(f"File not found")
