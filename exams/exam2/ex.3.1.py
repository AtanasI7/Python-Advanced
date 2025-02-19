def shopping_cart(*args):
    dishes = {}

    for el in args:
        if el == 'Stop':
            break

        type_of_meal = el[0]
        product_of_meal = el[1]

        if type_of_meal not in dishes:
            dishes[type_of_meal] = []
        dishes[type_of_meal].append(product_of_meal)


        if type_of_meal == 'Soup':
            if len(dishes[type_of_meal]) < 3:
                dishes[type_of_meal].append(product_of_meal)

        elif type_of_meal == 'Pizza':
            if len(dishes[type_of_meal]) < 4:
                dishes[type_of_meal].append(product_of_meal)

        elif type_of_meal == 'Dessert':
            if len(dishes[type_of_meal]) < 2:
                dishes[type_of_meal].append(product_of_meal)

    for key, value in dishes.items():
        dishes[key] = sorted(value)

    dishes = sorted(dishes.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    result = [f"{k}:\n  - {' '.join([x for x in v])}" for k, v in dishes]
    return '\n'.join(result)

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
