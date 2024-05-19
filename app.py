from flask import Flask, render_template, request, redirect, url_for, session
from controllers.register import RegisterManager
from controllers.login import LoginManager
from model import MySQLModel

app = Flask(__name__)
app.secret_key = "secret key"
@app.route('/')
def index():
    return render_template('index.html', title='Home', content='')
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
@app.route('/admin/article/create', methods=['GET', 'POST'])
def create_article():
    if 'admin' in session and session['admin'] == True:
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            mysql_model = MySQLModel()
            success, message = mysql_model.add_article(title, content)
            if success:
                return redirect(url_for('admin'))
            else:
                return message
        else:
            return render_template('admin/article/create.html', title='Create Article', content='')
    else:
        return redirect(url_for('login'))
@app.route('/admin/article/all')
def show_all_articles():
    mysql_model = MySQLModel()
    success, message = mysql_model.show_articles()
    if not success:
        return message
    articles = mysql_model.cursor.fetchall()
    return render_template('admin/article/all.html', title='All Articles', content=articles)
@app.route('/admin/article/edit/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    if 'admin' in session and session['admin'] == True:
        if request.method == 'POST':
            title = request.form.get('title')
            content = request.form.get('content')
            mysql_model = MySQLModel()
            success, message = mysql_model.edit_article(article_id, title, content)
            if success:
                return redirect(url_for('admin'))
            else:
                return message
        else:
            mysql_model = MySQLModel()
            success, message = mysql_model.show_articles()
            if not success:
                return message
            article = mysql_model.cursor.execute("SELECT * FROM articles WHERE id = %s", (article_id,))
            article = article.fetchone()
            return render_template('admin/article/edit.html', title='Edit Article', content=article)
    else:
        return redirect(url_for('login'))
    
@app.route('/admin/article/remove/<int:article_id>')
def remove_article(article_id):
    if 'admin' in session and session['admin'] == True:
        mysql_model = MySQLModel()
        success, message = mysql_model.remove_article(article_id)
        if success:
            return redirect(url_for('admin'))
        else:
            return message
    else:
        return redirect(url_for('login'))
    
@app.route('/admin/user/create', methods=['GET', 'POST'])
def create_user():
    if 'admin' in session and session['admin'] == True:
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            mysql_model = MySQLModel()
            success, message = mysql_model.add_user(username, password)
            if success:
                return redirect(url_for('admin'))
            else:
                return message
        else:
            return render_template('admin/user/create.html', title='Create User', content='')
    else:
        return redirect(url_for('login'))
    
@app.route('/admin/user/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if 'admin' in session and session['admin'] == True:
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            mysql_model = MySQLModel()
            success, message = mysql_model.edit_user(user_id, username, password)
            if success:
                return redirect(url_for('admin'))
            else:
                return message
        else:
            mysql_model = MySQLModel()
            success, message = mysql_model.show_users()
            if not success:
                return message
            user = mysql_model.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
            user = user.fetchone()
            return render_template('admin/user/edit.html', title='Edit User', content=user)
    else:
        return redirect(url_for('login'))
    
@app.route('/admin/user/remove/<int:user_id>')
def remove_user(user_id):
    if 'admin' in session and session['admin'] == True:
        mysql_model = MySQLModel()
        success, message = mysql_model.remove_user(user_id)
        if success:
            return redirect(url_for('admin'))
        else:
            return message
    else:
        return redirect(url_for('login'))
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
