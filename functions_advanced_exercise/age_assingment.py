def age_assignment(*args, **kwargs):
    result = []

    for name in args:
        for letter, age in kwargs.items():
            if name[0] == letter:
                result.append((name, age))

    final = [f"{x[0]} is {x[1]} years old" for x in result]

    return '\n'.join(sorted(final))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))