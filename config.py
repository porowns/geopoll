import os
basedir = os.path.abspath(os.path.dirname(__file__))


SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'geo.db')
SQLALCHEMY_MIGRATE_PRO = os.path.join(basedir, 'db_repository')
CSRF_ENABLED = True
SECRET_KEY = 'smelly-socks'
