states = ['nevada','arizona','california','utah']
print(states)
for state in states:
    print(f"Welcome to {state.title()}, Please make sure your seat belt is on!!!")
    print(f"Enjoy your trip!!!")
pizzas = ['dominos','papa johns','little caeser','pizza hut']
print(pizzas)
for pizza in pizzas:
    print(f"I like pepperoni pizza at {pizza.title()}!!")
print(f"I really love pizza !!")
for num in range(4, 8):
    print(num**2)
squares = []
for num in range(7, 18):
    squares.append(num**2)
print(squares)
print()

numbers = [2,45,78,63,525,369,457,1,7,25,9]
# print(numbers)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
#
# for num in range(1, 1000001):
#     print(num)
#     numbers.append(num)
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))
# # or
# numbers = list(range(1, 1000001))
# print(min(numbers))
# print(max(numbers))
# print(sum(numbers)
#
print(numbers)
new_copy = numbers
copied_numbers = numbers[:]
print(new_copy,numbers,copied_numbers)
numbers.append(5555)
print(new_copy,numbers,copied_numbers)
print("Sherzod Riskaliyev's HomeWork")
# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
grocery = ['onion','carrot','milk','lamb','chicken','bread']

# • Print the message, The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.
print('The first three items in the list are :')
for item in grocery[:3]:
    print(item.title())

# • Print the message, Three items from the middle of the list are:. Use a slice
# to print three items from the middle of the list.
print('The three items from middle of the list are :')
for item in grocery[2:5]:
    print(item.title())
# • Print the message, The last three items in the list are:. Use a slice to print
# the last three items in the list.
print('The last three items in the list are :')
for item in grocery[-3:]:
    print(item.title())
# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
my_pizzas = ['cheese','beef','hawaian','buffulo']
friend_pizza = my_pizzas[:]
print('My favorite pizza:')
print(my_pizzas)
print('My friends favorite pizza :')
print(friend_pizza)
# • Add a new pizza to the original list.
my_pizzas.append('chicken')
# • Add a different pizza to the list friend_pizzas.
friend_pizza.append('ham')
# • Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
#
# My friend’s favorite pizzas are:, and then use a for loop to print the sec-
# ond list. Make sure each new pizza is stored in the appropriate list.
print(my_pizzas)
print('My favorite pizza :')
for pizza in my_pizzas:
    print(pizza.title())
print(friend_pizza)
print('My friends favorite pizza :')
for pizza in friend_pizza :
    print(pizza.title())
# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.
my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
for food in my_foods :
    print(food.title())
print("\nMy friend's favorite foods are:")
for food in friend_foods :
    print(food.title())


print()
actor1 = {'name': 'tom','last name':'cruz','reward':'oscar','age': 40}
actor2 = {'name': 'leo','last name':'dicaprio','reward':'emmys','age': 36}
print(actor1['name'],actor1['reward'])
print(actor2['last name'],actor2['age'])
print(actor1)
print(actor2)
actor1['age'] = 57
print(actor1)
actor1['hometown'] = 'LA'
print(actor1)
del actor1['hometown']
print(actor1)
# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.

rivers = {'nile': 'egypt', 'hudson': 'usa', 'volga': 'russia', 'mississippi': 'usa', 'thames': 'uk'}
# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
for river, counrty in rivers.items():
    print(f"The {river.title()} runs through {counrty.title()}. ")


# • Use a loop to print the name of each river included in the dictionary.
for river in rivers.keys():
    print(river.title())

print()
# • Use a loop to print the name of each country included in the dictionary.
for counrty in rivers.values():
    print(counrty.title())


