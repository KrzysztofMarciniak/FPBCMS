import mysql.connector
from mysql.connector import Error

class MySQLModel:
    def __init__(self):
        self.connection = None
        self.cursor = None
    def insert_user(self, username, password):
        success, message = self.connect()
        if not success:
            return False, message
        try:
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            self.cursor.execute(query, (username, password))
            self.connection.commit()
            return True, "User added"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()

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
    def add_article(self, title, content):
        success, message = self.connect()
        if not success:
            return False, message
        try:
            query = "INSERT INTO articles (title, content) VALUES (%s, %s)"
            self.cursor.execute(query, (title, content))
            self.connection.commit()
            return True, "Article added"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
            
    def edit_article(self, article_id, title, content):
        success, message = self.connect()
        if not success:
            return False, message
        
        try:
            query = "UPDATE articles SET title = %s, content = %s WHERE id = %s"
            self.cursor.execute(query, (title, content, article_id))
            self.connection.commit()
            return True, "Article edited"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
            
    def remove_article(self, article_id):
        success, message = self.connect()
        if not success:
            return False, message
        
        try:
            query = "DELETE FROM articles WHERE id = %s"
            self.cursor.execute(query, (article_id,))
            self.connection.commit()
            return True, "Article removed"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
            
    def add_user(self, username, password):
        success, message = self.connect()
        if not success:
            return False, message
        
        try:
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            self.cursor.execute(query, (username, password))
            self.connection.commit()
            return True, "User added"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
    def show_article(self, article_id):
        success, message = self.connect()
        if not success:
            return False, message
        try:
            query = "SELECT * FROM articles WHERE id = %s"
            self.cursor.execute(query, (article_id,))
            article = self.cursor.fetchone()
            return True, article
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
    def edit_user(self, user_id, username, password):
        success, message = self.connect()
        if not success:
            return False, message
        
        try:
            query = "UPDATE users SET username = %s, password = %s WHERE id = %s"
            self.cursor.execute(query, (username, password, user_id))
            self.connection.commit()
            return True, "User edited"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
            
    def remove_user(self, user_id):
        success, message = self.connect()
        if not success:
            return False, message
        
        try:
            query = "DELETE FROM users WHERE id = %s"
            self.cursor.execute(query, (user_id,))
            self.connection.commit()
            return True, "User removed"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
            
    def get_titles_and_dates(self):
        success, message = self.connect()
        if not success:
            return False, message
        try:
            query = "SELECT id, date, title FROM articles"
            self.cursor.execute(query)
            titles_and_dates = self.cursor.fetchall()
            return True, titles_and_dates
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
    def get_id_from_title(self, article_title):
        success, message = self.connect()
        if not success:
            return False, message
        try:
            query = "SELECT id FROM articles WHERE title = %s"
            self.cursor.execute(query, (article_title,))
            article_id = self.cursor.fetchone()
            return True, article_id
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
    def get_content(self, article_title):
        success, message = self.connect()
        if not success:
            return False, message
        try:
            query = "SELECT content, title, date FROM articles WHERE title = %s"
            self.cursor.execute(query, (article_title,))
            article_content = self.cursor.fetchone()
            return True, article_content
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
    def edit_article(self, article_id, title, content):
        success, message = self.connect()
        if not success:
            return False, message
        try:
            query = "UPDATE articles SET title = %s, content = %s WHERE id = %s"
            self.cursor.execute(query, (title, content, article_id))
            self.connection.commit()
            return True, "Article edited"
        except mysql.connector.Error as err:
            return False, str(err)
        finally:
            self.disconnect()
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
