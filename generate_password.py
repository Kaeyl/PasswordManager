import random
import string

class Password_options:

    def weak_password(length):
        weak_selection = string.ascii_lowercase
        result_easy_string = ''.join(random.choice(weak_selection) for i in range(length))
        print("Your weak password containing", length, "characters is:", result_easy_string)
        return result_easy_string

    def medium_password(length):
        medium_password = string.ascii_lowercase + string.digits
        result_hard_string = ''.join(random.choice(medium_password) for i in range(length))
        print("Your strong password containing", length, "characters is:", result_hard_string)
        return result_hard_string

    def strong_password(length):
        strong_password = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        result_hard_string = ''.join(random.choice(strong_password) for i in range(length))
        print("Your strong password containing", length, "characters is:", result_hard_string)
        return result_hard_string
