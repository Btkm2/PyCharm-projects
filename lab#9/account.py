class account:
    def __init__(self,login,password,email):
        self.login = login
        self.password = password
        self.email = email
    def get_pass(self):
        return self.password
    def get_login(self):
        return self.login
    def get_email(self):
        return self.email