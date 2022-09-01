from flask import Blueprint
from .views import list_view, delete_view

todo_bp = Blueprint("todo", __name__, template_folder='templates',
                    static_folder='static', static_url_path='static')

todo_bp.add_url_rule("/", view_func=list_view, methods=["GET", "POST"])
todo_bp.add_url_rule(
    "/delete/<int:id>", view_func=delete_view, methods=["GET", "POST"])
