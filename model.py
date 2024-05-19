import mysql.connector

class MySQLModel:
    def __init__(self):
        self.connection = None

    def check_database_connection(self):
        self.connect()
        success = self.is_connected()
        message = "Connection is successful" if success else "Connection failed"
        self.disconnect()
        return success, message

    def connect(self, host='127.0.0.1', user='user', password='user', database='db'):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except mysql.connector.Error as err:
            raise err

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def is_connected(self):
        if self.connection:
            return self.connection.is_connected()
        return False

