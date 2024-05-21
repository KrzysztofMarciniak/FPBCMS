from flask import render_template, request, session, redirect, url_for
from model import MySQLModel
class EditManager:
    def __init__(self):
        pass

    def edit_form(self):
        return render_template('edit.html', title='Edit Page', content='')
