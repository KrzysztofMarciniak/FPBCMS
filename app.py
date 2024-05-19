from flask import Flask, render_template, request, redirect, url_for, session
from controllers.register import RegisterManager
from controllers.login import LoginManager
from model import MySQLModel

app = Flask(__name__)
app.secret_key = "secret key"
@app.route('/')
def index():
    return render_template('layout.html', title='Home', content='Welcome to the homepage!')
@app.route('/about')
def about():
    return render_template('layout.html', title='About', content='FPBCMS is a content management system.')
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_manager = LoginManager()
    if request.method == 'POST':
        return login_manager.login()
    else:
        return login_manager.show_form()
@app.route('/register', methods=['GET', 'POST'])
def register():
    register_manager = RegisterManager()
    if request.method == 'POST':
        return register_manager.register()
    else:
        return register_manager.show_form()
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('admin', None)
    return redirect(url_for('index'))
@app.route('/admin')
def admin():
    if 'admin' in session and session['admin'] == True:
        return render_template('admin/admin.html')
    else:
        return redirect(url_for('login'))

@app.route('/checkdb')
def check_db():
    mysql_model = MySQLModel()
    
    success, message = mysql_model.check_database_connection()
    if not success:
        return f'Error: {message}'
    
    success, message = mysql_model.ensure_tables_exist()
    if success:
        return f'Success: {message}'
    else:
        return f'Error: {message}'
    
if __name__ == '__main__':
    app.run(debug=True)
