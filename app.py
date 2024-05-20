from flask import Flask, render_template, request, redirect, url_for, session
from controllers.register import RegisterManager

from model import MySQLModel

from routes.index import index_bp
from routes.about import about_bp
from routes.login import login_bp
from routes.register import register_bp
from routes.articles import articles_bp

app = Flask(__name__)
app.secret_key = "secret key"
app.register_blueprint(index_bp)
app.register_blueprint(about_bp)
app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(articles_bp, url_prefix='/articles')


@app.route('/admin')
def admin():
    if 'admin' in session and session['admin'] == True:
        return render_template('admin/admin.html')
    else:
        return redirect(url_for('login.login'))

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
