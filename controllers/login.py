class LoginManager:
    def __init__(self):
        pass

    def login_user(self, username, password):
        if username == "admin" and password == "password":
            return True
        else:
            return False
