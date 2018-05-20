import os

basedir = os.path.abspath(os.path.dirname(__file__))

USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)

DATABASE = 'flask-taskr.db'
DATABASE_PATH = os.path.join(basedir, DATABASE)

print(DATABASE_PATH)
