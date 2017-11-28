from flask import render_template, json, request, flash, url_for, g, session
from flask_login import login_user, current_user, logout_user, login_required

from werkzeug.security import generate_password_hash
from werkzeug.utils import redirect
from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

from app import app, lm
from app.models.poll_whisperer import insert_new_poll
from app.models.table_declaration import User
from app.models.user_whisperer import insert_new_user, account_sign_in, user_query, user_exists


class signUpForm(Form):
    name = StringField('username', validators=[InputRequired(), Length(min=4,max=20)])
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8, max=50)])


class signInForm(Form):
    name = StringField('username or email', validators=[InputRequired(), Length(min=4,max=50)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])


@app.route('/')
def main():
    return render_template('homepage.html')


@app.route('/showSignUp', methods=['GET','POST'])
def showSignUp():
    form = signUpForm(request.form)
    if form.validate_on_submit():
        _hashed_pword = generate_password_hash(form.password.data,'sha256')
        _name = form.name.data
        _email = form.email.data

        if user_exists(_name) is False:
            insert_new_user(_name, _email, _hashed_pword)
            print('user: ' + _name + ' has been entered into the db')
            return redirect(url_for('main'))
        else:
            print("That username is already taken.")
    return render_template('signup.html', form=form)


@app.route('/showSignIn', methods=['GET','POST'])
def showSignIn():
    form = signInForm()
    if form.validate_on_submit():
        _acc_name = form.name.data
        _pword = form.password.data

        if g.user is not None and g.user.is_authenticated:
            print('user is already logged in')
            return redirect(url_for('user', user_name=g.user.user_name))

        q = account_sign_in(_acc_name, _pword)
        if q is not None:
            session['remember_me'] = q.user_id
            login_user(q)
            print('SignIn successful')
            return redirect(url_for('user', user_name=q.user_name))
        else:
            print('Invalid Information. Please try again.')
    return render_template('signin.html', form=form)


@app.route('/user/<user_name>', methods=['POST','GET'])
@login_required
def user(user_name):
    user = user_query(user_name, 1)
    return render_template('user.html', user=user)


@app.route('/showCreatePoll', methods=['POST'])
def showCreatePoll():
    # Get user from user query and replace this generic user
    _user = User('test', 'test', 'test')
    _poll_name = request.form['pollName']

    if _user and _poll_name:
        insert_new_poll(_poll_name, _user)
        return json.dumps({'html':'<span>All fields good!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/signout')
def signOut():
    logout_user()
    print('SignOut was Success')
    return redirect(url_for('main'))


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.before_request
def before_request():
    g.user = current_user




