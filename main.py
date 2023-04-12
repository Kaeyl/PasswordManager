import add_password
import delete
import update
import view

print("Please select from the following options: \n"
      "[1] View Passwords\n"
      "[2] Add Password\n"
      "[3] Edit Password\n"
      "[4] Edit Password and Email\n"
      "[5] Delete Password\n")
user_selection = input("What would you like to do? ")
if user_selection == "1":
    view.View()
    view.CopyToCLip()
if user_selection == "2":
    add_password.Add()
if user_selection == "3":
    update.UpdatePassword()
if user_selection == "4":
    update.UpdateAll()
if user_selection == "5":
    delete.Delete()