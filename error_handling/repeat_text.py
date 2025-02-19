text = input()


try:
    n_times = int(input())
    print(text * n_times)

except ValueError:
    print(f"Variable times must be an integer")