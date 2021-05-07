print("hello world ")
students = ['beck', 'khan', 'sherzod', 'shohista']
print(students)
print(students[3])
print('welcome'+ students[3] + ', How may I help you?')
print('welcome'+ students[3] + ', How may I help you?')
print('welcome '+ students[3].title() + ', How may I help you?')
print(f"welcome {(students[3]).title()} , How may I help you?")
cars = ['mazda','mercedes','lambo','ferrari','tesla','bugatti','rolls roys']
cars = ['mazda','mercedes','lambo','ferrari','tesla','bugatti','rolls roys']
print(cars)
print('I would like to own a ' + cars[4].title())
print(f"I would like to own a {(cars[4]).title()}")
print(f"I am giving my dad {(cars[6]).title()} as a gift!")
print(f"My wife has a {(cars[1]).title()}!")
cars = ['mazda','mercedes','lambo','ferrari','tesla','bugatti','rolls roys']
cars.append('lexus')
print(cars)
# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.
patients = ['ilon musk','mirziyoyev','ahad qayum','leo messi','jeff bezos']
print(patients)
print(f"Welcome {patients[0].title()}, I would like to invite you to my house for special dinner!")
print(f"Welcome {patients[1].title()}, I would like to invite you to my house for special dinner!")
print(f"Welcome {patients[2].title()}, I would like to invite you to my house for special dinner!")
print(f"Welcome {patients[3].title()}, I would like to invite you to my house for special dinner!")
print(f"Welcome {patients[4].title()}, I would like to invite you to my house for special dinner!")


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list.
print(patients)
print(f"Unfortunately, {patients[2].title()} can't make it to the dinner so I have to exclude him!")
patients.pop(2)
print(patients)
patients.insert(2,'queen elisabeth')
print(patients)
print(f"Welcome {patients[0].title()}, I would like to invite you to my house for special dinner!")
print(f"Welcome {patients[1].title()}, I would like to invite you to my house for special dinner!")
print(f"Welcome {patients[2].title()}, I would like to invite you to my house for special dinner!")
print(f"Welcome {patients[3].title()}, I would like to invite you to my house for special dinner!")
print(f"Welcome {patients[4].title()}, I would like to invite you to my house for special dinner!")
#
# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.
#
# Introducing Lists 47
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.
# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
# • Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.
#
# • Use sorted() to print your list in reverse alphabetical order without chang-
# ing the order of the original list.
#
# • Show that your list is still in its original order by printing it again.
# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.