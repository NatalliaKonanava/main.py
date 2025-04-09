"""
projekt_1.py: první projekt do Engeto Online Python Akademie (druhý pokus)

author: Natallia Konanava
email: nataxa_87@seznam.cz
"""
from collections import Counter

registered_users = [
    {"username": "bob", "password": "123"},
    {"username": "ann", "password": "pass123"},
    {"username": "mike", "password": "password123"},
    {"username": "liz", "password": "pass123"}
]

username = input("username: ")
password = input("password: ")
line = "-" * 40

user_found = False

for user in registered_users:
    if user["username"] == username and user["password"] == password:
        user_found = True
        break
print(line)

if user_found:
    print("Welcome to the app, ", username, "\n", "We have 3 texts to be analyzed.")
else:
    print("unregistered user, terminating the program..")
    exit()

print(line)

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


def draw_bar_chart(word_lengths):
    max_count = max(word_lengths.values(), default=0)

    for length, count in sorted(word_lengths.items()):
        print(f"{length:<3} | {'*' * count:<20} | {count}")


def analyze_text(TEXTS):
    import string
    words = TEXTS.split()
    cleaned_words = [word.strip(string.punctuation) for word in words]
    num_words = len(cleaned_words)  # total_words
    titlecase_words = [word for word in cleaned_words if word.istitle()]
    uppercase_words = [word for word in cleaned_words if word.isupper() and word.isalpha()]
    lowercase_words = [word for word in cleaned_words if word.islower()]
    numbers = [int(word) for word in cleaned_words if word.isdigit()]
    numbers_sum = sum(numbers)
    word_lengths = Counter(len(word.strip('.,!?()[]{}"')) for word in words)


    print("There are ", num_words, "words in the selected.")
    print("There are ", len(titlecase_words), "titlecase words.")
    print("There are ", len(uppercase_words), "uppercase words.")
    print("There are ", len(lowercase_words), "lowercase words.")
    print("There are ", len(numbers), "numeric strings.")
    print("The sum of all the numbers", numbers_sum)
    print(line)
    print(f"{'LEN':<3} | {'OCCURENCES':<20} | {'NR.'}")
    print(line)
    draw_bar_chart(word_lengths)

def main():
    choice = input("Enter a number btw. 1 and 3 to select: ".format(len(TEXTS)))
    print(line)

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(TEXTS):
            analyze_text(TEXTS[index])

        else:
            print("Invalid text number.")
            exit()

    else:
        print("Please, enter a number.")
        exit()

if __name__ == "__main__":
    main()