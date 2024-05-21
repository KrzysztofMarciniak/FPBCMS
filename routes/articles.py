from flask import Blueprint, render_template, request, redirect, url_for, session
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
@articles_bp.route('/new', methods=['GET', 'POST'])
def new():
    mysql_model = MySQLModel()
    if 'admin' in session and session['admin'] == True:
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            success, message = mysql_model.add_article(title, content)
            if not success:
                return message
            return redirect(url_for('articles.all'))
        else:
            return render_template('articles/new.html', title='New Article')
    else:
        return 'Access denied'
@articles_bp.route('/<article_title>/delete', methods=['POST'])
def delete(article_title):
    mysql_model = MySQLModel()
    if 'admin' in session and session['admin'] == True:
        success, message = mysql_model.delete_article(article_title)
        if not success:
            return message
        return redirect(url_for('articles.all'))
    else:
        return "Only admin can delete articles"


@articles_bp.route('/<article_title>/edit', methods=['GET', 'POST'])
def edit(article_title):
    mysql_model = MySQLModel()
    if 'admin' in session and session['admin'] == True:
        if request.method == 'POST':
            new_content = request.form['content']
            success, message = mysql_model.edit_article(article_title, new_content)
            if not success:
                return message
            return redirect(url_for('articles.read', article_title=article_title))
        else:
            success, message = mysql_model.connect()
            if not success:
                return message
            success, article = mysql_model.get_content(article_title)
            if not success:
                return article
            return render_template('articles/edit.html', title='Edit Article', content=article)
    else:
        return 'Access denied'
