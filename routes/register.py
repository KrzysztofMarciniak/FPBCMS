from flask import Blueprint, request
from controllers.register import RegisterManager

register_bp = Blueprint('register', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    register_manager = RegisterManager()
    if request.method == 'POST':
        return register_manager.register()
    else:
        return register_manager.show_form()