from flask import render_template, request, session, redirect, url_for
from model import MySQLModel
class LoginManager:
    def __init__(self):
        pass

    def show_form(self):
        return render_template('login.html', title='Login Page', content='')
    def login(self):
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            self.mysql_model = MySQLModel()
            success, message = self.mysql_model.authenticate_user(username, password)
            if success:
                session['username'] = username
                session['admin'] = True
                return redirect(url_for('index'))
            else:
                return message
        else:
            return self.show_form()