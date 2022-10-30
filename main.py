import random
import string

user_strength_selection = 0
user_length_selection = 0

class Password_options:

    def weak_password(length):
        weak_selection = string.ascii_lowercase
        result_easy_string = ''.join(random.choice(weak_selection) for i in range(length))
        print("Your weak password containing", length, "characters is:", result_easy_string)

    def medium_password(length):
        result_medium_string = ''.join(random.choice(string.ascii_letters)for i in range(length))
        print("Your medium password containing", length, "characters is:", result_medium_string)

    def strong_password(length):
        strong_password = string.ascii_lowercase + string.digits + string.punctuation
        result_hard_string = ''.join(random.choice(strong_password) for i in range(length))
        print("Your strong password containing", length, "characters is:", result_hard_string)

print("This is a simple password generator. Please select which complexity of password you would like to generate.\n"
      "An easy password consists of only alphabetical lowercase letters, with a minimum length of 8 characters.\n"
      "A medium password consists of lowercase and uppercase alphabetical characters with a minimum length of 12 characters.\n"
      "A hard password consists of lowercase, uppercase and special characters with a minimum length of 14 characters. \n"
      "You will be able to chose the length you want your password to be.\n\n")

def get_user_strength(selection):

    while True:
        try:
            user_input = int(input("please select from the following options: [1] Easy, [2] Medium, [3] Hard "))
        except:
            print("Input must be a number")
            continue
        if user_input == 1 or user_input == 2 or user_input == 3:
            selection = user_input
            return selection
        else:
            print('no valid response was found. Please select from the following options: [1] Easy, [2] Medium, [3] Hard')

def get_user_length_easy(selection):
    while True:
        try:
            user_input = int(input("please select how long your password will be. For an easy password it must be greater then 8: "))
        except:
            continue
        if user_input < 8:
            print('The value must be 8 or more')
        else:
            selection = user_input
            return selection

def get_user_length_medium(selection):
    while True:
        try:
            user_input = int(input("please select how long your password will be. For an easy password it must be greater then 12: "))
        except:
            continue
        if user_input < 12:
            print('The value must be 12 or more')
        else:
            selection = user_input
            return selection

def get_user_length_hard(selection):
    while True:
        try:
            user_input = int(input("please select how long your password will be. For an easy password it must be greater then 15: "))
        except:
            continue
        if user_input < 15:
            print('The value must be 15 or more')
        else:
            selection = user_input
            return selection

user_strength_selection = get_user_strength(user_strength_selection)

if user_strength_selection == 1:
    user_length_selection = get_user_length_easy(user_length_selection)
    Password_options.weak_password(user_length_selection)

if user_strength_selection == 2:
    user_length_selection = get_user_length_medium(user_length_selection)
    Password_options.medium_password(user_length_selection)

if user_strength_selection == 3:
    user_length_selection = get_user_length_hard(user_length_selection)
    Password_options.strong_password(user_length_selection)

