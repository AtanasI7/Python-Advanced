# text = sorted(input())
# char_and_its_count = {}
#
# # for el in text:
# #     if el not in char_and_its_count.keys():
# #         char_and_its_count[el] = 0
# #     char_and_its_count[el] += 1
# #
# # for key, value in char_and_its_count.items():
# #     print(f"{key}: {value} time/s")

text = input()
for i in sorted(set(text)):
    print(f"{i}: {text.count(i)} time/s")