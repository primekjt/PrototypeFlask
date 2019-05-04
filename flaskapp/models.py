# file name : models.py
# pwd : /project_name/app_name/models.py

from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __table_name__ = 'user'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(1000), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password, **kwargs):
        self.name = name
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return f"<User('{self.id}', '{self.name}', '{self.email}')>"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class tests(db.Model): #테이블명 및 테이블 정보
   id = db.Column('id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   city = db.Column(db.String(50))
   addr = db.Column(db.String(200))
   pin = db.Column(db.String(10))

if __name__ == "__main__":
    pass

"""
class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='your_password',
                                  db='your_dbname',
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit():
        self.db.commit()
"""

"""
Terminal -> sqlite3 Enter
sqlite> .open db.sqlite
sqlite>
drop table if exists user;
    create table user (
    id integer primary key autoincrement,
    name text not null,
    email text not null,    
    password text not null
);

INSERT INTO user (name,email,password) VALUES ('kim','kim@gmail.com','1234');
INSERT INTO user (name,email,password) VALUES ('Hong gi dong','hgd@gmail.com','1111');
"""