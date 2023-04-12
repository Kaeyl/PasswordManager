import connect
class Add:
    def __init__(self):
        password = input("What is your password? ")
        email = input("What is the email for this password? ")
        username = input("What is the username for this service? ")
        url = input("What is the url for this service? ")
        app = input("What is the app for this service? ")
        connect.add_password(password, email, username, url, app)
# Add()