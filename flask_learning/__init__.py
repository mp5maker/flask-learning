from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

def create_app():
    from .todo import todo_bp
    app.register_blueprint(todo_bp, url_prefix="")
    return app