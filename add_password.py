import connect
import generate_password

class Add:
    def __init__(self):
        user_selection = input("Would you like to manually apply a password 'm'  or randomly generate one? 'r' m/r ")
        if user_selection == "m":
            print("You have selected maniual password input")
            password = input("What is your password? ")
        if user_selection == "r":
            strength = input("How strong do you want the password to be? Weak = 1, Medium = 2, Strong = 3 " )
            length = int(input("How many characters do you want the password to contain? "))
            if strength == "1":
                password = generate_password.Password_options.weak_password(length)
            if strength == "2":
                password = generate_password.Password_options.medium_password(length)
            if strength == "3":
                password = generate_password.Password_options.strong_password(length)



        email = input("What is the email for this password? ")
        username = input("What is the username for this service? ")
        url = input("What is the url for this service? ")
        app = input("What is the app for this service? ")
        connect.add_password(password, email, username, url, app)
# Add()
