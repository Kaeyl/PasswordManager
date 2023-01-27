from password_options import Password_options, Password_save_options, Password_save_with_service_options
from create_key import Create_key, Encryption
from clear import Clear
import os
# ---------------------------------------------------------------------------------------------------------------------------------------
# This command is only here to  clear the user terminal before running. This it to reduce clutter
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
Clear.clear(Clear)
# ---------------------------------------------------------------------------------------------------------------------------------------
# This section will create a one time password. This password will be displayed and if not stored or saved, will be deleted
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
def create_one_time_use_password():
    strength = input("How strong do you want this password to be? [1] Weak [2] Moderate [3] Strong [b] to exit ")
    if strength != "":
        single_use_password_loop_check = False
        while single_use_password_loop_check == False:
            if strength == "1":
                while True:
                    try:
                        length = int(input('how many characters do you want this password to be? '))
                        break
                    except:
                        print("Please input a number ")
                single_use_password_loop_check = True
                Password_options.weak_password(int(length))
            if strength == "2":
                while True:
                    try:
                        length = int(input('how many characters do you want this password to be? '))
                        break
                    except:
                        print("Please input a number ")
                Password_options.medium_password(int(length))
                single_use_password_loop_check = True
            if strength == "3":
                while True:
                    try:
                        length = int(input('how many characters do you want this password to be? '))
                        break
                    except:
                        print("Please input a number ")
                single_use_password_loop_check = True
                Password_options.strong_password(int(length))
            if strength == "b":
                single_use_password_loop_check = True
    else:
        print("there is no valid response")
# ---------------------------------------------------------------------------------------------------------------------------------------
# This code will generate a password and it will save it to a file for later user.
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
def create_and_store_password():
    strength = input("How strong do you want this password to be? [1] Weak [2] Moderate [3] Strong [b] to exit ")
    if strength != "":
        create_and_store_loop_check = False
        while create_and_store_loop_check == False:
            if strength == "1":
                while True:
                    try:
                        length = int(input('how many characters do you want this password to be? '))
                        break
                    except:
                        print("Please input a number ")
                create_and_store_loop_check = True
                Password_save_options.weak_password(int(length))
            if strength == "2":
                while True:
                    try:
                        length = int(input('how many characters do you want this password to be? '))
                        break
                    except:
                        print("Please input a number ")
                create_and_store_loop_check = True
                Password_save_options.medium_password(int(length))
            if strength == "3":
                while True:
                    try:
                        length = int(input('how many characters do you want this password to be? '))
                        break
                    except:
                        print("Please input a number ")
                create_and_store_loop_check = True
                Password_save_options.strong_password(int(length))
            if strength == "b":
                create_and_store_loop_check = True
                break
    else:
        print("there is no valid response")
# ---------------------------------------------------------------------------------------------------------------------------------------
# This code will create a password for the user, but it will also take an additional perameter which will take the service that the user
# wants that password to be stored as. The service will be anything that the user needs the password for: Facebook, gmail, twitter etc.
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
def create_and_store_password_with_service():
    service = input("what service is this password for? ")
    strength = input("How strong do you want this password to be? [1] Weak [2] Moderate [3] Strong [b] to exit ")
    if strength != "":
        create_and_store_with_service_loop_check = False
        while create_and_store_with_service_loop_check == False:
            if strength == "1":
                while True:
                    try:
                        length = int(input('how many characters do you want this password to be? '))
                        break
                    except:
                        print("Please input a number ")
                create_and_store_with_service_loop_check = True
                Password_save_with_service_options.weak_password_with_service(int(length), service)
            if strength == "2":
                while True:
                    try:
                        length = int(input('how many characters do you want this password to be? '))
                        break
                    except:
                        print("Please input a number ")
                create_and_store_with_service_loop_check = True
                Password_save_with_service_options.medium_password_with_service(int(length), service)
            if strength == "3":
                while True:
                    try:
                        length = int(input('how many characters do you want this password to be? '))
                        break
                    except:
                        print("Please input a number ")
                create_and_store_with_service_loop_check = True
                Password_save_with_service_options.strong_password_with_service(int(length), service)
            if strength == "b":
                exit()
    else:
        print("there is no valid response")
# ---------------------------------------------------------------------------------------------------------------------------------------
# This will allow the user to check existing passwords.
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
def view_stored_passwords():
    # Encryption.decrypt("user_passwords.txt", "key.key")
    view_password_file = open("user_passwords.txt")
    lines = view_password_file.readlines()
    for i in lines:
        print(i.splitlines())
    view_password_file.close()
# ---------------------------------------------------------------------------------------------------------------------------------------
# This section checks to see if the user has previously set a password.
# By doing this, we can vaLidate that the program has not been run before as the program requires this password to continue
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
def check_if_user_has_password_set():
    if os.path.getsize('password.txt') == 0:
        print("It looks like this is the first time you are running this app!")
        user_pass_input = input("Please enter a primary user password: ")
        file_write_pass = open("password.txt", "a")
        Create_key.write_key("private.key")
        file_write_pass.write(user_pass_input)
        file_write_pass.close()
        print("Password has been set. User password is now: " + user_pass_input)
        Encryption.encrypt("password.txt", "private.key")
# ---------------------------------------------------------------------------------------------------------------------------------------
# This section asks the user for a password if it is a valid password it will run. Otherwise it will terminate the program
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
def pass_validate():
    if os.path.getsize('password.txt') > 0:
        validated = False
        max_attempts = 0
        print("there is a password")
        Encryption.decrypt("password.txt", "private.key")
        open_file = open('password.txt', 'r')
        passwds = open_file.readlines()
        while validated == False:
            user_validate_passwd = input("Please enter your primary user password: ")
            if user_validate_passwd in passwds:
                print("found")
                Encryption.encrypt("password.txt", "private.key")
                validated = True
            elif user_validate_passwd not in passwds:
                print("your password does not match!")
                max_attempts += 1
            if max_attempts == 3:
                print("Password entered incorrectly too many times. Quitting...")
                Encryption.encrypt("password.txt", "private.key")
                quit()
    else:
        print("a password has not been found")
# ---------------------------------------------------------------------------------------------------------------------------------------
# This is the start to the running part of the program. This will execute the program in a loop until the user quits or enters
# a password incorrect too many times.
#---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
continue_program = True
check_if_user_has_password_set()
print("Welcome to the simple password manager. This is a basic program that will allow the user to create store and manage passwords.")
while continue_program:
    Clear.clear(Clear)
    print("""                                                                               
                                 ..               ....              ...                                 
                               .JPGP?        :~7JY5GGPPY?~:       .J5PP7                                
                               ^BBBBG.     !5BBGGBB#B#BBBBGY~     ^BBB#G.                               
                                ^YBJ:    ^5BBBBBPY?77?YPBBBBBY.    ^YB?:                                
                                 !B^    :GBBBB5^       .!PBBBB5.    7#^                                 
                         .::     7#?!~  YBBBBY           .PBBB#7 .!!Y#^     ::.                         
                        JGBG5:   :!!!~ .PBBBB~            ?BBBBY .!!!!.   ~PBBG7                        
                       .PBBBB^.JY7~!!~ .PBBBB~            ?BBBBY  ~!!!?5? 7BBBBY                        
                        .7BJ. .JY7!!7~ .PBBBB~            ?BBBBY .!7!!?5?  :PG~                         
                         :BY~!!!!!!!!~ .PBBBB~            ?BBBBY  ~!~~~!!!!!PG                          
             :^^.        .~~!77!77777~  PBBBB~            ?BBBBY  !!!!!77777!!         .^^.             
            JBBBP7!!!!!!!~~~~~~!.   ^7YYGBBBB5JJYYYYYYYYYYPBBBBGYJ7:   ^!~~~~~!!!!!!!!?GGGG7            
            5BBBG?7777777!!!!777: .YBBBBBBBBGGBBBBBBBBBBBBBBBBBBBBBB?  ^77777777777777JGBBB?            
             ^~~.   :~~~~~~~~~~~: ~#BBBBBBBBGBBBBBBBGBBBBBBBBBBBBBBBB: ^~~~~~~~~~~~.   :~~:             
                    JB?777777777: !BBBBBBBBBBBBBP7^::~?GBBBBBBBBBBBBB: ~777777777J#!                    
                   .YB^  ~J?~~~~: !BBBBBBBBBBBBP.      ^BBBBBBBBBBBBG: ^~~~!JJ:  !#?                    
                  ~GBBBY 7PY7777: !BBBBBBBBBBBBP.      ^BBBBBBBBBBBBG: ~777?55~.PBBBP:                  
                  ~GBBBJ    ^~~~. !BBBBBBBBBBBBBP7.  :?GBBBBBBBBBBBBB: :~~^:   .5BBBP:                  
                   .^^:     PG??^ !BBBBBBBBBBBBBBB^  !#BBBBBBBBBBBBBB: ~??BY     :^^                    
                            5Y    !BBBBBBBBBBBBGGG7.:YBBBBBBBBBBBBBBB:    GJ                            
                           ^PP^   !BBBBBBBBBBG55P5PGGBBBBBBBBBBBBBBBG:   !B5^                           
                          JBBB#?  ^GBBBBBBBBBGPPPPPBBBBBBBBBBBBBBBBB5.  5#BBB!                          
                          !PGGP~   ^JPGGGGGGGBGGGGBGGGGGGGGGGGGGGP5?.   7PGG5^                          
                           .::       .:::::::::::::::::::::::::::.       .::        
                           \n""")
    print("Please select an option to continue:\n[1]: Create a once off password\n[2]: Store a password \n[3]: Delete an existing password\n[4]: View passwords\n[q]: Exit")
    user_selection = input("What would you like to do? ")
    if user_selection != "":
# ---------------------------------------------------------------------------------------------------------------------------------------
# This will allow a user to create a one time password that will not be saved. It will be immediately forgotten when the user closes the
# program or chooses another command
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
        if user_selection == "1":
            create_one_time_use_password()
            create_single_once_off_password_continue = True
            while create_single_once_off_password_continue:
                user_continue = input("would you like to make another password? y/n ")
                if user_continue == 'y':
                    create_one_time_use_password()
                    continue
                elif user_continue == "n":
                    create_single_once_off_password_continue = False
                    break
                else:
                    print("this is not acceptable input")
# ---------------------------------------------------------------------------------------------------------------------------------------
# This section allows the user to assign an encryption key for their passwords before alloing them to create and store one.
# The user will then be able to assign a ppassword and a service. The service is a website or platform in which the user wishes
# to create the password for.
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
        if user_selection == "2":
            option_create_new_key = input("Would you like to create a new key? y/n ")
            if option_create_new_key == "y":
                final_confirmation = input("this will overide existing keys and make previously stored passwords unreadable. Are you sure you want to continue? y/n ")
                if final_confirmation == 'y':
                    pass_validate()
                    Encryption.decrypt("user_passwords.txt", "key.key")
                    Create_key.write_key("key.key")
                    Encryption.encrypt("user_passwords.txt", "key.key")
                else:
                    print("Key has not been changed. ")
            else:
                print("no Key has been created. Using existing key")
            # ---------------------------------------------------------------------------------------------------------------------------------------
            # This will allow the user to create passwords until they choose to stop. The file must be decrypted to be able to store passwords to it
            # It must also be encrypted after use.
            # the first if statement checks to see if there is any information in the document. If there is, it will decrypt. if there is not it will
            # not decrypt the information as this creates an issue with fernet. There must be information within the file to be able to decrypt and
            # encrypt.
            # ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
            create_more_passwords = True
            store_password_loop_continue = True
                # ---------------------------------------------------------------------------------------
                # Here we must make sure that there are passwords stored in the password file.
                # If there are not then we can not decrypt. User must store passwords first.
                # -----------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓-----------------------------
            if os.path.getsize('user_passwords.txt') > 0:
                while store_password_loop_continue:
                    option_add_service = input("would you like to save a service to this password? y/n ")
                    if option_add_service == "y":
                        Encryption.decrypt("user_passwords.txt", "key.key")
                        create_and_store_password_with_service()
                        Encryption.encrypt("user_passwords.txt", "key.key")
                        user_continue = input("would you like to make another password? y/n ")
                        if user_continue == "n":
                            store_password_loop_continue = False
                        else:
                            continue
                    if option_add_service == "n":
                        Encryption.decrypt("user_passwords.txt", "key.key")
                        create_and_store_password()
                        Encryption.encrypt("user_passwords.txt", "key.key")
                        user_continue = input("would you like to make another password? y/n ")
                        if user_continue == "n":
                            store_password_loop_continue = False
                        else:
                            continue
                # ---------------------------------------------------------------------------------------
                # This block of code will run if there are no stored passwords.
                # -----------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓-----------------------------
            else:
                while store_password_loop_continue:
                    option_add_service = input("would you like to save a service to this password? y/n ")
                    if option_add_service == "y":
                        create_and_store_password_with_service()
                        # Encryption.encrypt("user_passwords.txt", "key.key")
                        user_continue = input("would you like to make another password? y/n ")
                        if user_continue == "n":
                            Encryption.encrypt("user_passwords.txt", "key.key")
                            store_password_loop_continue = False
                        else:
                            continue
                    if option_add_service == "n":
                        create_and_store_password()
                        # Encryption.encrypt("user_passwords.txt", "key.key")
                        user_continue = input("would you like to make another password? y/n ")
                        if user_continue == "n":
                            Encryption.encrypt("user_passwords.txt", "key.key")
                            store_password_loop_continue = False
                        else:
                            continue
# ---------------------------------------------------------------------------------------------------------------------------------------
# This section allows the user to view existing passwords and then it will number the passwords and allow the user to delete
# a password based on its position in the list.
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
        if user_selection == "3":
            view_passwords = input("Are you sure you want to delete a password? y/n ")
            if view_passwords == "y":
                # ---------------------------------------------------------------------------------------
                # Here the code must check to see if there are passwords stored in the stored password
                # file. If there are not then it will force the user back to the main page.
                # ---------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓--------------------------------
                if os.path.getsize('user_passwords.txt') > 0:
                    Encryption.decrypt("user_passwords.txt", "key.key")
                    open_file = open('user_passwords.txt', 'r')
                    file_lines = open_file.readlines()
                # ---------------------------------------------------------------------------------------
                # This for loop will iterate over each line of the file
                # -----------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓-----------------------------
                    count = 0
                    for line in file_lines:
                        count += 1
                        print("[{}]: {}".format(count, line.strip()))
                # ---------------------------------------------------------------------------------------
                    delete_loop_continue = True
                # ---------------------------------------------------------------------------------------
                # This loop will run to allow the user to create multiple passwords.
                # -----------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓-----------------------------
                    while delete_loop_continue == True:
                        try:
                            delete_password = input("which password would you like to delete? q to return to home: ")
                            if delete_password.isdigit():
                                pass
                            if delete_password == "":
                                print("can not be empty")
                                continue
                            if delete_password == "q":
                                Encryption.encrypt("user_passwords.txt", "key.key")
                                delete_loop_continue = False
                                break
                        except:
                            print("Please input a number ")
                # ---------------------------------------------------------------------------------------
                # This section will confirm that the user wants to delete this password before
                # deleting it.
                # -----------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓-----------------------------
                        while delete_loop_continue:
                            user_delete_confirmation = input("are you sure you want to delete password at postion " + str(delete_password) + "? y/n ")
                            if user_delete_confirmation == 'y':
                                count = 0

                                for line in file_lines:
                                    count += 1
                                    if count == delete_password:
                                        print("[{}]: {}".format(delete_password, line.strip() + " has been deleted"))

                                delete_password = int(delete_password) - 1

                                with open(r"user_passwords.txt", 'r') as fp:
                                    # read and store all lines into list
                                    lines = fp.readlines()
                                # Write file
                                with open(r"user_passwords.txt", 'w') as fp:
                                    # iterate each line
                                    for number, line in enumerate(lines):
                                        if number not in [delete_password]:
                                            fp.write(line)
                                user_continue = input("would you like to delete another? y/n ")
                # ---------------------------------------------------------------------------------------
                # If the user choses no, the informatino will be encrypted, the loop will be broken and
                # the user will be returned to the main menu.
                # -----------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓-----------------------------
                                if user_continue == "n":
                                    Encryption.encrypt("user_passwords.txt", "key.key")
                                    delete_loop_continue = False
                                    break
                                else:
                # ---------------------------------------------------------------------------------------
                # This is the loop that will allow the user to keep deleting. This is messy code and
                # will be edited and tidied up later.
                # -----------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓-----------------------------
                                    while delete_loop_continue == True:
                                        try:
                                            delete_password = input("which password would you like to delete? q to return to home: ")
                                            if delete_password.isdigit():
                                                break
                                            if delete_password == "q":
                                                Encryption.encrypt("user_passwords.txt", "key.key")
                                                delete_loop_continue = False
                                                break

                                            else:
                                                print("something went wrong")
                                                continue
                                        except:
                                            print("input is invalid")
                            else:
                                print("You have chosen not to delete this password")
                                delete_loop_continue = False
                else:
                    print("there are no passwords stored. We can not delete anything")
                    print("going back to the main screen...")
            elif view_passwords == "n":
                print("not showing passwords")
# ---------------------------------------------------------------------------------------------------------------------------------------
# This section allows the user to simply view all stored passwords.
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
        if user_selection == "4":
            Encryption.decrypt("user_passwords.txt", "key.key")
            view_stored_passwords()
            Encryption.encrypt("user_passwords.txt", "key.key")
            user_continue = input("would you like to return to the home screen and run another command? y/n ")
            if user_continue == 'y':
                continue
            else:
                print("Goodbye")
                continue_program = False
# ---------------------------------------------------------------------------------------------------------------------------------------
# This section allows the user to quit
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
        if user_selection == 'q':
            print("Goodbye")
            continue_program = False

# ---------------------------------------------------------------------------------------------------------------------------------------
# If the user does not put in any inpur (presses enter repeatedly) this message will appear.
# ---------------------------------------------↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓---------------------------------------------
    else:
        print("nothing was selected ")



