# -*- coding: UTF-8 -*-
# file name : config.py
# pwd : /project_name//app_name/config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ADMIN_EMAIL = "your_email@gmail.com"

    # Define the application directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_NAME = 'flaskapp'
    SECRET_KEY = 'write-a-secret-string-here'
    LISTINGS_PER_PAGE = 5

    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_HASH = 'pbkdf2:sha256'
    SECURITY_PASSWORD_SALT = 'add_salt_0701_hard_one'
    SECURITY_CONFIRMABLE = True


    # SendGrid example.
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_SSL = False
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'username'
    MAIL_PASSWORD = 'password'
    DEFAULT_MAIL_SENDER = 'notifications@your_website.com'
    SECURITY_EMAIL_SENDER = 'notifications@your_website.com'

    RECAPTCHA_SITE_KEY = "CRSxxxxxxxxxxxxxxxxxxxxxxx"
    RECAPTCHA_SECRET = "CRSCRSxxxxxxxxxxxxxxxxxxxxxxxx"



class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@server_ip:server_port/db_name'
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    TESTING = True