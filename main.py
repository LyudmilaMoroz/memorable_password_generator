import random
from words_list import data

symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
special_symbols_dict = {'E':'%', 'T':'&', 'A':'@', 'O':'()', 'I':'!', 'N':'#', 'S':'$'}

##TODO: Get password rules from user
print("Welcome to the Memorable Password Generator!")
password_type = input("What type of password do you want to create? words or phrase\n").capitalize()
words_amount = int(input("How many words you want in your password?\n"))
replace_letters = input("Would you like to replace some common letters with special characters: True or False?\n").capitalize()
add_numbers = input("Add numbers: True or False\n").capitalize()
numbers_amount = int(input("How many numbers you want in your password?\n"))
add_symbols = input("Add special characters: True or False\n").capitalize()
symbols_amount = int(input("How many symbols you want in your password?\n"))

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


def replace_letters_to_symbols(password, special_symbols_dict):
    for key in special_symbols_dict:
        value = special_symbols_dict[key]
        password = password.replace(key, value).replace(key.lower(), value)
    return password


def add_numbers_to_password(password, numbers_amount):
    for n in range(numbers_amount):
        number = str(random.randint(0,9))
        add = random.randint(0,1)
        if add == 0:
            password = number + password
        else:
            password = password + number
    return password


def add_symbols_to_password(password, symbols_list, symbols_amount):
    for n in range(symbols_amount):
        random_symbol = random.choice(symbols_list)
        password += random_symbol
    return password


def show_password(password):
    print(f"Your new password: {password}")


if password_type == "Words":
    generated_password = create_words_password(words_amount)
elif password_type == "Phrase":
    generated_password = create_phrase_password(words_amount)

if replace_letters == "True":
    generated_password = replace_letters_to_symbols(generated_password, special_symbols_dict)

if add_numbers == "True":
    generated_password = add_numbers_to_password(generated_password, numbers_amount)

if add_symbols == "True":
    generated_password = add_symbols_to_password(generated_password, symbols_list, symbols_amount)

show_password(generated_password)

