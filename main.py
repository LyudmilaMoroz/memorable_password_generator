import random
from words_list import data

symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# E -> %, T -> &, A -> @, O -> (), I -> !, N -> #, S -> $

##TODO: Get password rules from user
print("Welcome to the Meaningful Password Generator!")
password_type = input("What type of password do you want to create? words or phrase\n").lower()
words_amount = int(input("How many words you want in your password?\n"))
add_numbers = bool(input("Add numbers: True or False\n").upper())
numbers_amount = int(input("How many numbers you want in your password?\n"))
add_symbols = bool(input("Add special characters: True or False\n").upper())
symbols_amount = int(input("How many symbols you want in your password?\n"))
#replace_letters = bool(input("Would you like to replace some common letters with special characters?\n").upper())

#TODO: Get information from the website (when user clicks "Generate password")
#TODO: Generate password

def create_words_password(words_amount):
    password = ""
    for n in range(words_amount):
        random_word = random.choice(data)[0]
        password += random_word.capitalize()
    return password


def create_phrase_password(words_amount):
    random_words = random.choices(data, k=words_amount)
    list = []
    for word in random_words:
        list += word
    phrase_password = "-".join(list)
    return phrase_password


def add_numbers_to_password(password, numbers_amount):
    for n in range(numbers_amount):
        number = str(random.randint(0,9))
        password += number
    return password


def add_symbols_to_password(password, symbols_list, symbols_amount):
    for n in range(symbols_amount):
        random_symbol = random.choice(symbols_list)
        password += random_symbol
        print(generated_password)
    return password


def show_password(password):
    print(f"just created: {password}")


if password_type == "words":
    generated_password = create_words_password(words_amount)
elif password_type == "phrase":
    generated_password = create_phrase_password(words_amount)

if add_numbers:
    generated_password = add_numbers_to_password(generated_password, numbers_amount)

if add_symbols:
    generated_password = add_symbols_to_password(generated_password, symbols_list, symbols_amount)

show_password(generated_password)

#if replace_letters:
#    # Replace all letters from the given words
#    print("Replace letters")

