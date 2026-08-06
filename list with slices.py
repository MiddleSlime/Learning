peoples = ['Gagarin', 'Joseph', 'Julian', 'Shkibidi', 'Man1', 'Man2', 'Man3']
print(peoples[2:4])
print(peoples[:2])
print(peoples[-1:])

print(f'The first three elements are: {peoples[:3]}')
print(f'The middle 2 elements: {peoples[2:5]}')
print(f'The last 3 elements: {peoples[-3:]}')
# Task with pizzas
my_pizza = ['pepperoni', 'mushroom']
friend_pizza = ['pineapple', 'cheese']
my_pizza = friend_pizza[:]
my_pizza.append('pizzawithicecream')
friend_pizza.append('shkibidini')
for pizza in my_pizza:
    print(f'My favourite pizza is {pizza}')
for pizza1 in friend_pizza:
    print(f'My favourite pizza is {pizza1}')

# Tuple? What is Tuple?

age_differences = (18, 27)
print(age_differences)
for age in age_differences:
    print(age)

age_differences = (19, 28)
print(age_differences)
for age in age_differences:
    print(age)