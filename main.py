import random

weak_pass = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
medium_pass = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
strong_pass = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","_","-"]
very_strong_pass = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","@","#","$","%","^","&","*","_","-",":",";"]

user_pass = []
user_final_password = []


def full_program():
    class ProgramGenerator():
        while True:
            try:
                user_input = (int(input('''How strong do you want this password?
                Please enter a value equal to the strength of this password 1 = weak
                4 = very strong
                ''')))
                if user_input > 0 and user_input < 5:
                    user_pass.clear()
                    break
            except ValueError:
                print("Please enter a valid number!")
                continue
            else:
                print("not valid")


        print("You have submitted a valid number")
        number_of_characters = (int(input("How many charaters do you want the password to be? ")))





        def weak_password():
            random_password = random.choice(weak_pass)
            random_pass_generator = random.choice(weak_pass)
            user_pass.append(random_pass_generator)
        if user_input == 1:
                for i in range(number_of_characters):
                    weak_password()
        else:
            pass


        divider = ""
        display_weak_password = divider.join(user_pass)


        def medium_password():
            random_password = random.choice(medium_pass)
            random_pass_generator = random.choice(medium_pass)
            user_pass.append(random_pass_generator)
        if user_input == 2:
                for i in range(number_of_characters):
                    medium_password()
        else:
            pass


        divider = ""
        display_medium_password = divider.join(user_pass)


        def strong_password():
            random_password = random.choice(strong_pass)
            random_pass_generator = random.choice(strong_pass)
            user_pass.append(random_pass_generator)
        if user_input == 3:
                for i in range(number_of_characters):
                    strong_password()
        else:
            pass


        divider = ""
        display_strong_password = divider.join(user_pass)


        def very_strong_password():
            random_password = random.choice(very_strong_pass)
            random_pass_generator = random.choice(very_strong_pass)
            user_pass.append(random_pass_generator)

        if user_input == 4:
                for i in range(number_of_characters):
                    very_strong_password()

        else:
            pass


        print("[+] Generating your very strong password")
        divider = ""
        display_password = divider.join(user_pass)
        print(display_password)



    ProgramGenerator()


full_program()


def continue_or_not():

    while True:
        try:
            user_decision = input("Would you like to generate more passwords? ")
            user_decision = user_decision.upper()
            if user_decision == "NO" or user_decision == "N":
                break
            if user_decision == "YES" or user_decision == "Y":
                full_program()
        except ValueError:
            print("Please enter a valid number!")
            continue



continue_or_not()
