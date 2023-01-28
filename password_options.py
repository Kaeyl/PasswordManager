import random
import string
# ---------------------------------------------------------------------------------------------------------------------------------------
# This class allows the user to create a password that will be forgotten after user. This password will increase in complexity depending
# on the option the user selects.
# Weak passwords only user lowercase ascii characters.
# Medium strength user lowercase ascii characters and numbers.
# Strong passwords will utilise ascii characters as well as special characters.
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
class Password_options:

    def weak_password(length):
        weak_selection = string.ascii_lowercase
        result_easy_string = ''.join(random.choice(weak_selection) for i in range(length))
        print("Your weak password containing", length, "characters is:", result_easy_string)

    def medium_password(length):
        medium_password = string.ascii_lowercase + string.digits
        result_hard_string = ''.join(random.choice(medium_password) for i in range(length))
        print("Your strong password containing", length, "characters is:", result_hard_string)

    def strong_password(length):
        strong_password = string.ascii_lowercase + string.digits + string.punctuation
        result_hard_string = ''.join(random.choice(strong_password) for i in range(length))
        print("Your strong password containing", length, "characters is:", result_hard_string)

# ---------------------------------------------------------------------------------------------------------------------------------------
# This class will create a password for the user and then save it. This password will increase in complexity depending
# on the option the user selects.
# Weak passwords only user lowercase ascii characters.
# Medium strength user lowercase ascii characters and numbers.
# Strong passwords will utilise ascii characters as well as special characters.
# The program will then write the password to a file
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
class Password_save_options:

    def weak_password(length):
        weak_selection = string.ascii_lowercase
        result_easy_string = ''.join(random.choice(weak_selection) for i in range(length))
        print("Your weak password containing", length, "characters is:", result_easy_string)
        f = open("user_passwords.txt", "a")
        f.write(result_easy_string + "\n")
        f.close()

    def medium_password(length):
        medium_password = string.ascii_lowercase + string.digits     #
        result_hard_string = ''.join(random.choice(medium_password) for i in range(length))     #
        print("Your strong password containing", length, "characters is:", result_hard_string)
        f = open("user_passwords.txt", "a")
        f.write(result_hard_string + "\n")
        f.close()

    def strong_password(length):
        strong_password = string.ascii_lowercase + string.digits + string.punctuation     #
        result_hard_string = ''.join(random.choice(strong_password) for i in range(length))
        print("Your strong password containing", length, "characters is:", result_hard_string)
        f = open("user_passwords.txt", "a")
        f.write(result_hard_string + "\n")
        f.close()
# ---------------------------------------------------------------------------------------------------------------------------------------
# This class will create a password for the user and then save it and allow the user to save a service i.e. a website.
# This password will increase in complexity depending on the option the user selects.
# Weak passwords only user lowercase ascii characters.
# Medium strength user lowercase ascii characters and numbers.
# Strong passwords will utilise ascii characters as well as special characters.
# The program will then write the password to a file
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
class Password_save_with_service_options:

    def weak_password_with_service(length, service):
        if service == "":
            print("there was no services provided")
        else:
            weak_selection = string.ascii_lowercase     #
            result_easy_string = ''.join(random.choice(weak_selection) for i in range(length))     #
            print("Your weak password containing", length, "characters is:", result_easy_string)   #
            f = open("user_passwords.txt", "a")
            f.write(service + ", " + "[" + result_easy_string + "]" + "\n")
            f.close()

    def medium_password_with_service(length, service):
        if service == "":
            print("there was no services provided")
        else:
            medium_password = string.ascii_lowercase + string.digits     #
            result_hard_string = ''.join(random.choice(medium_password) for i in range(length))     #
            print("Your strong password containing", length, "characters is:", result_hard_string)
            f = open("user_passwords.txt", "a")
            f.write(service + ", " + "[" + result_hard_string + "]" + "\n")
            f.close()

    def strong_password_with_service(length, service):
        if service == "":
            print("there was no services provided")
        else:
            strong_password = string.ascii_lowercase + string.digits + string.punctuation     #
            result_hard_string = ''.join(random.choice(strong_password) for i in range(length))
            print("Your strong password containing", length, "characters is:", result_hard_string)
            f = open("user_passwords.txt", "a")
            f.write(service + ", " + "[" + result_hard_string + "]" + "\n")
            f.close()
