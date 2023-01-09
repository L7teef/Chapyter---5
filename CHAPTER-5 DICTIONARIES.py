##1.                                 Use a dictionary to store information about a person you know.Store their first name, last name, age, and the city in which they live. You
#                                             should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

#ANSWER : 

# person = {
#     'first_name': 'Mohammed',
#     'last_name': 'Abdullateef',
#     'age': 18,
#     'city': 'Abu Dhabi',
#     }

# print(person['first_name'])
# print(person['last_name'])
# print(person['age'])
# print(person['city'])

##2.                       A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
#                  Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store 
#                                                                their meanings as values.
#                   Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print 
#                   the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between 
#                                                        each word-meaning pair in your output.


#ANSWER :

# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     }

# word = 'string'
# print("\n" + word.title() + ": " + glossary[word])
# word = 'comment'
# print("\n" + word.title() + ": " + glossary[word])
# word = 'list'
# print("\n" + word.title() + ": " + glossary[word])
# word = 'loop'
# print("\n" + word.title() + ": " + glossary[word])
# word = 'dictionary'
# print("\n" + word.title() + ": " + glossary[word])


##3.               Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
#                 calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms 
#                         to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.

#ANSWER : 

# glossary = {
#     'string': 'A series of characters.',
#     'comment': 'A note in a program that the Python interpreter ignores.',
#     'list': 'A collection of items in a particular order.',
#     'loop': 'Work through a collection of items, one at a time.',
#     'dictionary': "A collection of key-value pairs.",
#     'key': 'The first item in a key-value pair in a dictionary.',
#     'value': 'An item associated with a key in a dictionary.',
#     'conditional test': 'A comparison between two values.',
#     'float': 'A numerical value with a decimal component.',
#     'boolean expression': 'An expression that evaluates to True or False.',
#     }

# for word, definition in glossary.items():
#     print("\n" + word.title() + ": " + definition)

##4.                   Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#                                         * Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#                                                * Use a loop to print the name of each river included in the dictionary.
#                                               * Use a loop to print the name of each country included in the dictionary.


#ANSWER :

# rivers = {
#     'nile': 'egypt',
#     'Ganga': 'india',
#     'Bhramaputra': 'india',
#     'kaveri': 'india',
#     'yangtze': 'china',
#     }

# for river, country in rivers.items():
#     print("The " + river.title() + " flows through " + country.title() + ".")

# print("\nThe following rivers are included in this data set:")
# for river in rivers.keys():
#     print("- " + river.title())

# print("\nThe following countries are included in this data set:")
# for country in rivers.values():
#     print("- " + country.title())

##5.Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
# owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about 
# each pet

#ANSWER :

## Make individual pets, and store each one in the list.
# pets = []
# pet = {
#     'animal type': 'Cat',
#     'name': 'peanut',
#     'owner': 'Lateef',
#     'weight': 43,
#     'eats': 'Whiskas',
# }
# pets.append(pet)

# pet = {
#     'animal type': 'Dog',
#     'name': 'Jacky',
#     'owner': 'Gavin',
#     'weight': 35,
#     'eats': 'Pedigree',
# }
# pets.append(pet)

# pet = {
#     'animal type': 'dog',
#     'name': 'Diamond',
#     'owner': 'Saif',
#     'weight': 37,
#     'eats': 'Royal Canin',
# }
# pets.append(pet)

## Display information about each pet.
# for pet in pets:
#     print("\nHere's what I know about " + pet['name'].title() + ":")
#     for key, value in pet.items():
#         print("\t" + key + ": " + str(value))