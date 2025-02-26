
registered_users = [
    {"username": "bob", "password": "123"},
    {"username": "ann", "password": "pass123"},
    {"username": "mike", "password": "password123"},
    {"username": "liz", "password": "pass123"}
]

username = input("username: ")
password = input("password: ")

user_found = False

for user in registered_users:
    if user["username"] == username and user["password"] == password:
        user_found = True
        break

if user_found:
    print("Welcome to the app, ", username, "\n", "We have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

text = input("Enter a number btw. 1 and 3 to select:")

if text == "1":
    print(TEXTS[0])
    words = TEXTS[0].split()
    num_words = len(words)
    print("There are ", num_words, "words in the selected.")
    res = len([word for word in words if word[0].isupper()])
    print("There are ", res, "titlecase words.")
    big = 0
    for word in words:
        if word.isupper():
            big += 1
    print("There are ", big, "uppercase words.")
    little = 0
    for word in words:
        if word.islower():
            little += 1
    print("There are ", little, "lowercase words.")
    count = 0
    for word in words:
        if word.replace(".", "", 1).isdigit():
            count += 1
    print("There are ", count, "numeric strings.")
    total = 0
    for word in words:
        if word.replace(".", "", 1).isdigit():
            total += int(word)
    print("The sum of all the numbers", total)

elif text == "2":
    print(TEXTS[1])
    words = TEXTS[1].split()
    num_words = len(words)
    print("There are ", num_words, "words in the selected.")
    res = len([word for word in words if word[0].isupper()])
    print("There are ", res, "titlecase words.")
    big = 0
    for word in words:
        if word.isupper():
            big += 1
    print("There are ", big, "uppercase words.")
    little = 0
    for word in words:
        if word.islower():
            little += 1
    print("There are ", little, "lowercase words.")
    count = 0
    for word in words:
        if word.replace(".", "", 1).isdigit():
            count += 1
    print("There are ", count, "numeric strings.")
    total = 0
    for word in words:
        if word.replace(".", "", 1).isdigit():
            total += int(word)
    print("The sum of all the numbers", total)


    #num_words = len(words)
    #print("There are ", num_words, "words in the selected.")
    #res = len([word for word in words if word[0].isupper()])
    #print("There are ", res, "titlecase words.")
    #cap = len([word for word in words if word[0].upper()])
    #print("There are ", cap, "titlecase words.")

elif text == "3":
    print(TEXTS[-1])
    words = TEXTS[-1].split()
    num_words = len(words)
    print("There are ", num_words, "words in the selected.")
    res = len([word for word in words if word[0].isupper()])
    print("There are ", res, "titlecase words.")
    big = 0
    for word in words:
        if word.isupper():
            big += 1
    print("There are ", big, "uppercase words.")
    little = 0
    for word in words:
        if word.islower():
            little += 1
    print("There are ", little, "lowercase words.")
    count = 0
    for word in words:
        if word.replace(".", "", 1).isdigit():
            count += 1
    print("There are ", count, "numeric strings.")
    total = 0
    for word in words:
        if word.replace(".", "", 1).isdigit():
            total += int(word)
    print("The sum of all the numbers", total)



    #num_words = len(words)
    #print("There are ", num_words, "words in the selected.")
    #res = len([word for word in words if word[0].isupper()])
    #print("There are ", res, "titlecase words.")
    #cap = len([word for word in words if word[0].upper()])
    #print("There are ", cap, "titlecase words.")

else:
    print("Konec")