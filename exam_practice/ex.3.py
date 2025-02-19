def softuni_students(*args, **kwargs):
    passed_dict = {}
    invalid_people = []
    for el in args:
        id = el[0]
        username = el[1]

        for key, value in kwargs.items():
            if id == key:
                if value not in passed_dict.keys():
                    passed_dict[value] = username
                else:
                    passed_dict[value] += username
            else:
                invalid_people.append(username)

    passed_dict = dict(sorted(passed_dict.items(), key=lambda x: x[1]))
    result = [f"*** A student with the username {person} has successfully finished the course {course}" for course, person in passed_dict.items()]
    invalid_result = [f"!!! Invalid course students: {[x for x in invalid_people]}"]
    print(*result, sep='\n')
    print(*invalid_result, sep='\n')


# print(softuni_students(
#     ('id_1', 'Kaloyan9905'),
#     id_1='Python Web Framework',
# ))


# print(softuni_students(
#     ('id_7', 'Silvester1'),
#     ('id_32', 'Katq21'),
#     ('id_7', 'The programmer'),
#     id_76='Spring Fundamentals',
#     id_7='Spring Advanced',
# ))


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
