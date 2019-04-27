# file name : config.py
# pwd : /project_name//app_name/config.py
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__)) #Use this for relative directory representation

SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIR,'blog.sqlite')

SECRET_KEY = "CRSCCCRRRRRRSSSSSSSSSSS"