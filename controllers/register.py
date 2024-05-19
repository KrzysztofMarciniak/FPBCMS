from flask import render_template, request, redirect, url_for
import mysql.connector
from model import MySQLModel
class RegisterManager:
    def __init__(self):
        self.mysql_model = MySQLModel()

    def show_form(self):
        return render_template('register.html', title='Register Page', content='')

    def register(self):
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            request_secret_password = request.form.get('secret_password')
            secret_password = "pass"
            if secret_password == request_secret_password:
                self.mysql_model.connect()
                
                try:
                    cursor = self.mysql_model.connection.cursor()
                    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                    self.mysql_model.connection.commit()
                except mysql.connector.Error as err:
                    print(f"Error: {err}")
                    raise err
                finally:
                    cursor.close()
                    self.mysql_model.disconnect()
                return redirect(url_for('login'))
            else:
                return "Wrong secret password"
                

