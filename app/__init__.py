from flask import Flask
import sqlite3

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    return app
