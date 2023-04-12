import connect
import view

class UpdatePassword:
    def __init__(self):
        view.View()
        position_id = input("Which password would you like to update? 'choose by selecting the position number' ")
        password = input("what is the new password? ")

        # delete.Delete(position_id)
        connect.edit_password(position_id, password)

class UpdateAll:
    def __init__(self):
        view.View()
        position_id = input("Which password would you like to update? 'choose by selecting the position number' ")
        password = input("what is the new password? ")
        email = input("What is the new email address? ")
        username = input("What is the new username? ")
        url = input("What is the new URL? ")
        app = input("What is the new APP? ")
        connect.edit_row(password, email, username, url, app, position_id)