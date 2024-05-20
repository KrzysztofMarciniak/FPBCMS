from flask import Blueprint, render_template
from model import MySQLModel  

articles_bp = Blueprint('articles', __name__)

@articles_bp.route('/')
def all():
    mysql_model = MySQLModel()
    success, message = mysql_model.connect()
    if not success:
        return message
    success, articles = mysql_model.get_titles_and_dates()
    if not success:
        return articles 
    return render_template('articles/list.html', title='All Articles', content=articles)
@articles_bp.route('/<article_title>/read')
def read(article_title):
    mysql_model = MySQLModel()
    success, message = mysql_model.connect()
    if not success:
        return message
    success, article = mysql_model.get_content(article_title)
    if not success:
        return article
    return render_template('articles/read.html', title='Read', content=article)