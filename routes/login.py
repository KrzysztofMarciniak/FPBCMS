from flask import Blueprint, request, session, redirect, url_for
from controllers.login import LoginManager

login_bp = Blueprint('login', __name__)
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    login_manager = LoginManager()
    if request.method == 'POST':
        return login_manager.login()
    else:
        return login_manager.show_form()
@login_bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('admin', None)
    return redirect(url_for('index.index'))