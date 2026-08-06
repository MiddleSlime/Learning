uzbeki = ["Amir", 'WIvan', 'WKostikSmerch']
for uzbek in uzbeki: #We can choose anything for the first thing
    print(f'I really like your focuses Mr.{uzbek}!')
print('Thank you for everything!Nice to meet you!')

# 4-1 Pizzas:
pizzas = ['Pepperoni', 'pineapple shit', 'Yummy', 'Mushroom']
for pizza in pizzas:
    print(f'I am so fucking like {pizza}!')
print(f'But I am liying about {pizzas[1]}')
# 4-2 Animals
animals = ['cow', 'platypus', 'femboy']
for animal in animals:
    print(f'{animals} provide very yummy milk))')
print(f'But man I really like all of these')

# RAaaaaaaange
for value in range(0, 6):
    print(value)
numbers = list(range(1,5))
print(numbers)
even_numbers = list(range(2, 12, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
# squares = [value**2 for value in range(1, 11)]
# print(squares) The same, but more cooler ouuuu

units = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(units))
print(max(units))
print(sum(units))


