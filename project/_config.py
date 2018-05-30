import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)

DATABASE = 'flask-taskr.db'
DATABASE_PATH = os.path.join(basedir, DATABASE)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
