def cookbook(*args):
    culinary_book = []
    for elms in args:
        recipe_name = elms[0]
        cuisine = elms[1]
        ingredients = elms[2]


    sorted_culinary_book = dict(sorted(culinary_book.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))



print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
))
