class DBConnection:
    instance = None

    def __new__(cls, *args):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


    def __init__(self, password, login):
        self.password = password
        self.login = login

p = 'admin'
login = 'admin'

d = DBConnection(p, login)
print(d)

d2 = DBConnection(p, login)
print(d2)