class Credentials:
    def __init__(self):
        self.host = 'localhost'
        self.port = '5432' 
        self.user = 'postgres'
        self.password = 'admin'
        self.db_name = 'postgres'

    def get_host(self):
        return self.host

    def get_port(self):
        return self.port

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def get_db_name(self):
        return self.db_name
