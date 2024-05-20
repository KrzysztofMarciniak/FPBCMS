from flask import Blueprint, render_template

about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    return render_template('layout.html', title='About', content='FPBCMS is a Basic Content Management System, Powered by Flask!')