def shopping_cart(*args):
    counter = 0
    dishes = {'Soup': [],
              'Pizza': [],
              'Dessert': []
              }

    for el in args:
        if el == 'Stop':
            break

        type_of_meal = el[0]
        products_of_meal = el[1]

        if type_of_meal == 'Soup':
            if products_of_meal not in dishes[type_of_meal]:
                if len(dishes[type_of_meal]) < 3:
                    dishes[type_of_meal].append(products_of_meal)

        elif type_of_meal == 'Pizza':
            if products_of_meal not in dishes[type_of_meal]:
                if len(dishes[type_of_meal]) < 4:
                    dishes[type_of_meal].append(products_of_meal)

        elif type_of_meal == 'Dessert':
            if products_of_meal not in dishes[type_of_meal]:
                if len(dishes[type_of_meal]) < 2:
                    dishes[type_of_meal].append(products_of_meal)

    for key, value in dishes.items():
        dishes[key] = sorted(value)

    result = ''

    for product in dishes.values():
        if len(product) == 0:
            counter += 1

    if counter == 3:
        return f"No products in the cart!"

    sorted_dishes = sorted(dishes.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for type_of_meal, products_of_meal in sorted_dishes:
        result += f"{type_of_meal}:\n"
        for product in products_of_meal:
            result += f" - {product}\n"
    return result


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))


print(shopping_cart(
            ('Pizza', 'ham'),
            ('Dessert', 'milk'),
            ('Pizza', 'ham'),
            'Stop',
        ))
