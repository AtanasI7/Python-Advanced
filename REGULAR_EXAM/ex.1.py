from collections import deque

money_amount = [int(x) for x in input().split()]
food_prices = deque([int(x) for x in input().split()])

eaten_food = 0

while money_amount and food_prices:
    money_el = money_amount[-1]
    price_el = food_prices[0]

    if money_el == price_el:
        eaten_food += 1
        money_amount.pop()
        food_prices.popleft()

    elif money_el > price_el:
        eaten_food += 1
        change = money_el - price_el
        if len(money_amount) != 1:
            money_amount.pop()
            money_amount[-1] += change
        else:
            money_amount[-1] = change

        food_prices.popleft()

    elif money_el < price_el:
        money_amount.pop()
        food_prices.popleft()

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")

if 1 < eaten_food < 4:
    print(f"Henry ate: {eaten_food} foods.")

if eaten_food == 1:
    print(f"Henry ate: {eaten_food} food.")

# if eaten_food < 4:
#     if eaten_food == 1:
#         print(f"Henry ate: {eaten_food} food.")
#     else:
#         print(f"Henry ate: {eaten_food} foods.")

if eaten_food == 0:
    print(f"Henry remained hungry. He will try next weekend again.")