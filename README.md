# Geopoll.io
Python project for CIS 4930.

**Project Title:** Geopoll.io

**Geopoll.io** will be a polling web application (similar to strawpoll), where users can create surveys to gather geolocation data and demographics about a community. We will utilize the Google Maps API for geolocation. It will be a Flask web application (w/ SQLAlchemy) with the following,

- Randomly generated urls for unique polls

- Geolocation input for users

- Demographic input for users

- Results page showing anonymized summary of the answers

# Installation 
1. Install Python and get Pip
2. Run `sudo pip3 install flask, flask_login, flask_sqlalchemy, flask_bootstrap, flask_wtf, sqlalchemy_utils`
3. `cd geopoll`
4. `python3 run.py`
5. Open 127.0.0.1:5000 in your web browser.
