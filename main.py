import random
import string

user_strength_selection = 0
user_length_selection = 0

class Password_options:

    def weak_password(length):
        weak_selection = string.ascii_lowercase     #here we are using string.ascii_lowercase, this is to allow the random function to select from alphabetical lowercase only
        result_easy_string = ''.join(random.choice(weak_selection) for i in range(length))     #here we are taking a randomly selected number of characters and joining them together,
        print("Your weak password containing", length, "characters is:", result_easy_string)   #The for loop will then repeat this selection for the total of the number selected by the user.

    def medium_password(length):
        medium_password = string.ascii_lowercase + string.digits     #The medium strength uses alphanumeric values. It does the same thing as the function above
        result_hard_string = ''.join(random.choice(medium_password) for i in range(length))     #but it selects from a numeric value as well.
        print("Your strong password containing", length, "characters is:", result_hard_string)

    def strong_password(length):
        strong_password = string.ascii_lowercase + string.digits + string.punctuation     #In the strong password section, characters are also available from the special characters catagory.
        result_hard_string = ''.join(random.choice(strong_password) for i in range(length))
        print("Your strong password containing", length, "characters is:", result_hard_string)

# This message will show when the user launches the program. This is the simple explinations and directions for the user.
print("This is a simple password generator. Please select which complexity of password you would like to generate.\n"
      "An easy password consists of only alphabetical lowercase letters, with a minimum length of 8 characters.\n"
      "A medium password consists of lowercase and uppercase alphabetical characters with a minimum length of 12 characters.\n"
      "A hard password consists of lowercase, uppercase and special characters with a minimum length of 14 characters. \n"
      "You will be able to chose the length you want your password to be.\n\n")

# Here the user will be able to select the strength of the password to be generated. 1 being a weak password with only alphabetical characters,
# 2 being a moderately strong password containing alphanumerical characters and 3 being the strongest password with alphanumeric and special characters.
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

# Here the user will be able to select what length they want their password to be. For easy, it must be alphabetical and the length must be 8 or greater.
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

# For medium strength the password must and alphanumeric and be 12 or greater.
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

# For strong passwords, the length must be 15 or greater and contain all characters.
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

# Here we are simply using an if statement to select the right method of execution.
if user_strength_selection == 1:
    user_length_selection = get_user_length_easy(user_length_selection)
    Password_options.weak_password(user_length_selection)

if user_strength_selection == 2:
    user_length_selection = get_user_length_medium(user_length_selection)
    Password_options.medium_password(user_length_selection)

if user_strength_selection == 3:
    user_length_selection = get_user_length_hard(user_length_selection)
    Password_options.strong_password(user_length_selection)

# ____________________________________________________________________________________________________________________ #
# Possible future expansion for this program includes an ability to save and store the password.
