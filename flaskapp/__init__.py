# file name : __init__.py
# pwd : /project_name/app_name/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

#def create_app():
app = Flask(__name__)

#app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

""" .py file을 통한 설정 """
#app.config.from_pyfile('config.py')

""" config object(class)를 통한 설정 {module}.{class}"""
app.config.from_object('config.DevelopmentConfig')

print('BASE_DIR: ' + app.config['BASE_DIR'])
print('SQLALCHEMY_DATABASE_URI: ' + app.config['SQLALCHEMY_DATABASE_URI'])

""" DB init """
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))
    #return User.query.filter(User.id == int(user_id)).first()

# blueprint for auth routes in our app
from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

#print(app.url_map)

#    return app

#if __name__ == "__main__":
#    app = create_app()
