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
                success, message = self.mysql_model.insert_user(username, password)
                if success:
                    return redirect(url_for('login.login'))
                else:
                    return message
            else:
                return "Wrong secret password"
        else:
            return self.show_form()
        

