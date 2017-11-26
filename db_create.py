#!flask/bin/python
from app import db

# If geo.db already exists in ./geopoll, then this script does not need to run!
db.create_all()



