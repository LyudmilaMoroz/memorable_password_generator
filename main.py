import random
from words_list import data

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# E -> %, T -> &, A -> @, O -> (), I -> !, N -> #, S -> $

##TODO: Get password rules from user
print("Welcome to the Meaningful Password Generator!")
password_type = input("What type of password do you want to create?\n")
words_amount = int(input("How many words you want in your password?\n"))
#add_numbers = bool(input("Add numbers: True or False\n").upper())
#numbers_amount = int(input("How many numbers you want in your password?\n"))
#add_symbols = bool(input("Add special characters: True or False\n").upper())
#symbols_amount = int(input("How many numbers you want in your password?\n"))
#replace_letters = bool(input("Would you like to replace some common letters with special characters?\n").upper())

#TODO: Get information from the website (when user clicks "Generate password")
#TODO: Generate password

def create_words_password(words_amount, password):
    for n in range(words_amount):
        random_word = random.choice(data)[0]
        password += random_word.capitalize()
    return password


def create_phrase_password(words_amount, password):
    random_words = random.choices(data, k=words_amount)
    list = []
    for word in random_words:
        list += word
    phrase_password = "-".join(list)
    return phrase_password


def show_password():
    print(f"just created: {new_generated_password}")


password = ""
if password_type == "words_password":
    new_generated_password = create_words_password(words_amount, password)
elif password_type == "phrase_password":
    new_generated_password = create_phrase_password(words_amount, password)

show_password()

#if add_numbers:
#    # Generate string with n amount of numbers according to "numbers_amount" input.
#    print("Add numbers")

#if add_symbols:
#    # Generate string with n amount of special symbols according to "symbols_amount) input.
#    print("Add symbols")

#if replace_letters:
#    # Replace all letters from the given words
#    print("Replace letters")

