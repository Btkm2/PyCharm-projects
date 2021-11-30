class account:
    def __init__(self,login,password):
        self.login = login
        self.password = password
    def get_pass(self):
        return self.password
    def get_login(self):
        return self.login