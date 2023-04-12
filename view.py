from tabulate import tabulate
import pyperclip
import connect

class View:
    def __init__(self):
        captured_list = connect.view()
        print(tabulate(captured_list, headers=["ID","Password", "Email", "User", "URL", "App"]))
        print("\n")

class CopyToCLip:
    def __init__(self):
        # ===============================Copy to Clipboard===================================
        # Select which position you want to copy with []
        captured_list = connect.view()
        copy_password = input("would you like to copy a password to the clipboard? y/n ")
        if copy_password == 'y':
            position_selected = input("please select which password position you would like to copy from? ")
            for i in captured_list:
                if i[0] == int(position_selected):
                    password = i[1]
                    pyperclip.copy(str(password))
                    print("Copied: ", password, " to clipboard")
                    break
                if i[0] != int(position_selected):
                    pass

        else:
            print("No valid selections were made")