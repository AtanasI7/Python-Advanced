def negative_vs_positive(numbers):
    positive = 0
    negative = 0

    for el in numbers:
        if el > 0:
            positive += el
        else:
            negative += el
    print(negative)
    print(positive)

    if positive < abs(negative):
        print(f"The negatives are stronger than the positives")
    else:
        print(f"The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]

negative_vs_positive(numbers)