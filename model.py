import mysql.connector

class MySQLModel:
    def __init__(self):
        self.connection = None
        self.cursor = None
    def authenticate_user(self, username, password):
        success, message = self.connect()
        if not success:
            return False, message
        
        try:
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            self.cursor.execute(query, (username, password))
            user = self.cursor.fetchone()
            if user:
                return True, "User authenticated"
            else:
                return False, "Invalid username or password"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
            
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='127.0.0.1',
                user='user',
                password='user',
                database='db'
            )
            self.cursor = self.connection.cursor()
            return True, "Connection established"
        except mysql.connector.Error as err:
            return False, str(err)

    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            self.connection = None

    def check_database_connection(self):
        success, message = self.connect()
        if success:
            self.disconnect()
        return success, message

    def ensure_tables_exist(self):
        success, message = self.connect()
        if not success:
            return success, message
        
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) NOT NULL,
                    password VARCHAR(255) NOT NULL
                )
            """)

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS articles (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    title VARCHAR(255) NOT NULL,
                    content TEXT NOT NULL
                )
            """)

            self.connection.commit()
            return True, "Tables ensured"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
