from flask import render_template, json, request, flash, url_for, g, session
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import redirect

from app import app, lm
from app.models.table_declaration import User
from app.models.user_whisperer import insert_new_user, account_sign_in, user_query


@app.route('/')
def main():
    return render_template('homepage.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    # read the posted values
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _pword = request.form['inputPassword']

    # validate values
    if _name and _email and _pword:
        print('_name',_name)
        print('_email',_email)
        print('_pword',_pword)
        insert_new_user(_name, _email, _pword)
        return json.dumps({'html': '<span>All fields good!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')


@app.route('/signIn', methods=['POST','GET'])
def signIn():
    _acc_name = request.form['inputAccName']
    _pword = request.form['inputPassword']

    if _acc_name and _pword:
        # user is already logged in
        if g.user is not None and g.user.is_authenticated:
            return(redirect('/'))
        else:
            q = account_sign_in(_acc_name, _pword)
            # if user exists in our database
            # log them in by storing their
            # information in current session
            # session object runs as long as
            # application is running
            remember_me = False
            if q is not None:
                session['remember_me'] = q
                login_user(q)
                print("SUCCESS")
                return redirect('user')

            #print(q.user_email)
            #user(q.user_id)
        return json.dumps({'html':'<span>All fields good!</span>'})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/signout')
def signOut():
    logout_user()
    return redirect(url_for('homepage'))


@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/user/<user_id>')
@login_required
def user(user_name):
    user = user_query(user_name)
    if user is None:
        flash('User not found')
        return redirect(url_for('homepage'))
    return render_template('user.html', user=user)

