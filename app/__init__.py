from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'db'
app.config['MYSQL_HOST'] = 'mysql'

mysql = MySQL(app)

@app.route('/')
def index():
    return 'Welcome to my Flask app!'
@app.route('/records/create')
def create_records():
    cur = mysql.connection.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL
        )
    """)
    
    usernames = ['user1', 'user2', 'user3', 'user4', 'user5']
    for username in usernames:
        cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
    
    mysql.connection.commit()
    cur.close()
    
    return 'Users table created and records inserted successfully!'

@app.route('/records')
def get_records():
    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM users")
    rows = cur.fetchall()
    cur.close()
    
    results = []
    for row in rows:
        results.append({'username': row[0]})

    return jsonify(results)
