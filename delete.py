import connect
import view


class Delete:
    def __init__(self):
        view.View()
        user_selection = input("Which password would you like to delete? ")
        postgres_insert_query = """ DELETE FROM password_table WHERE p_id = (%s);"""
        connect.delete_password(user_selection, postgres_insert_query)
        print("This will delete the password")

