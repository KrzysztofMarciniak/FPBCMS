from flask import Blueprint, render_template
from model import MySQLModel  

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
        mysql_model = MySQLModel()
        success, message = mysql_model.connect()
        if not success:
            return message
        success, articles = mysql_model.get_titles_and_dates()
        if not success:
            return articles 
        return render_template('articles/list.html', title='All Articles', content=articles)