from copy import deepcopy


def cookbook(*args):
    culinary_book = {}
    for elms in args:
        recipe_name = elms[0]
        cuisine = elms[1]
        ingredients = elms[2]

        if cuisine not in culinary_book.keys():
            culinary_book[cuisine] = {}

        culinary_book[cuisine][recipe_name] = ingredients

    sorted_culinary_book = dict(sorted(culinary_book.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))
    copy_sorted_culinary_book = deepcopy(sorted_culinary_book)

    for key, value in copy_sorted_culinary_book.items():
        values = dict(sorted(value.items()))
        sorted_culinary_book[key] = values

    result = ''

    for cuisine, recipe_name in sorted_culinary_book.items():
        result += f'{cuisine} cuisine contains {len(recipe_name)} recipes:\n'
        for recipe, ingredients in recipe_name.items():
            result += f"  * {recipe} -> Ingredients: {', '.join(ingredients)}\n"

    return result

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))

# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))
#
# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
#     ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
#     ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
#     ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
#     ))

