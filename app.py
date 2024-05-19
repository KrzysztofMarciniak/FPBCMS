from flask import Flask, render_template
from model import MySQLModel

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('layout.html', title='Home', content='Welcome to the homepage!')
@app.route('/login')
def login():
    return render_template('layout.html', title='Login Page', content='Login!')

@app.route('/about')
def about():
    return render_template('layout.html', title='About', content='FPBCMS is a content management system.')
    
@app.route('/checkdb')
def check_db():
    mysql_model = MySQLModel()
    success, message = mysql_model.check_database_connection()
    if success:
        return f'Success: {message}'
    else:
        return f'Error: {message}'
if __name__ == '__main__':
    app.run(debug=True)
