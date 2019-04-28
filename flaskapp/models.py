# file name : models.py
# pwd : /project_name/app_name/models.py

from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

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