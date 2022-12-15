from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os

db = SQLAlchemy()
DB_NAME = "database.db"





def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dajdlksjdl klsjdlja'
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    db_uri = 'sqlite:///{}'.format(db_path)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)
    
    return app

def create_database(app): 
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!') 

