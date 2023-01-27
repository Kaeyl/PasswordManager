import random
import string

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

class Password_save_options:

    def weak_password(length):
        weak_selection = string.ascii_lowercase     #here we are using string.ascii_lowercase, this is to allow the random function to select from alphabetical lowercase only
        result_easy_string = ''.join(random.choice(weak_selection) for i in range(length))     #here we are taking a randomly selected number of characters and joining them together,
        print("Your weak password containing", length, "characters is:", result_easy_string)   #The for loop will then repeat this selection for the total of the number selected by the user.
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